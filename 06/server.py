import argparse
import json
import socket
import threading

from typing import Callable
from collections import Counter
from bs4 import BeautifulSoup
import requests


def count_top_frequent_words(url, k: int) -> str:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, features="html.parser")
    count = dict(Counter(soup.get_text().split()))

    top_frequent = {}
    for key in sorted(count, reverse=True, key=lambda x: count[x])[:k]:
        top_frequent[key] = count[key]

    return json.dumps(top_frequent, indent=4, ensure_ascii=False)


class Master(threading.Thread):
    def __init__(self, workers: int, func: Callable, *func_args):
        super(Master, self).__init__()
        self.workers = workers
        self.semaphore = threading.Semaphore(workers)

        self.func = func
        self.func_args = func_args

        self.serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
        self.serv_sock.bind(("127.0.0.1", 53210))
        self.serv_sock.listen()

    def run(self):
        while True:
            client_sock, _ = self.serv_sock.accept()

            self.semaphore.acquire()
            client_thread = threading.Thread(
                target=self.handle_client, args=(client_sock,)
            )
            client_thread.start()

    def handle_client(self, client_sock):
        while True:
            data = client_sock.recv(1024)
            if not data:
                break

            url = data.decode()
            try:
                result = self.func(url, *self.func_args)
                client_sock.sendall(result.encode())
            except Exception as e:
                client_sock.sendall("error".encode())
                client_sock.close()
                print(f"Ошибка: {e}")
            finally:
                self.semaphore.release()


if __name__ == "__main__":
    argument_parser = argparse.ArgumentParser(
        "Server",
        "Multithreading app for scraping urls to get top K frequent words",
    )
    argument_parser.add_argument(
        "-w", default=None, type=int, help="workers amount", required=True
    )
    argument_parser.add_argument(
        "-k", default=None, type=int, help="search for k frequent words", required=True
    )

    args = argument_parser.parse_args()
    workers, words = args.w, args.k

    server = Master(workers, count_top_frequent_words, words)
    server.start()
