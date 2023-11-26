import argparse
import json
import socket
import threading

from typing import Callable
from collections import Counter
from bs4 import BeautifulSoup
import requests

from concurrent.futures import ThreadPoolExecutor


def count_top_frequent_words(url, k: int) -> str:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, features="html.parser")
    count = dict(Counter(soup.get_text().split()))

    top_frequent = {}
    for key in sorted(count, reverse=True, key=lambda x: count[x])[:k]:
        top_frequent[key] = count[key]

    return json.dumps(top_frequent, indent=4, ensure_ascii=False)


class Master:
    def __init__(self, workers: int, func: Callable, *func_args):
        self.func = func
        self.func_args = func_args
        self.url_count = 0
        self.url_count_lock = threading.Lock()
        self.executor = ThreadPoolExecutor(max_workers=workers)

        self.serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
        self.serv_sock.bind(("127.0.0.1", 53210))
        self.serv_sock.listen(10)

    def run(self):
        while True:
            client_sock, _ = self.serv_sock.accept()
            self.executor.submit(self.handle_client, client_sock)

    def handle_client(self, client_sock):
        try:
            data = client_sock.recv(1024)
            if not data:
                return

            url = data.decode()
            result = self.func(url, *self.func_args)
            client_sock.sendall(result.encode())
        except Exception as e:
            client_sock.sendall("error".encode())
            print(f"Ошибка: {e}")
        finally:
            client_sock.close()
            with self.url_count_lock:
                self.url_count += 1
                print(f"Обработано URL: {self.url_count}")


if __name__ == "__main__":
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument("-w", type=int, required=True, help="workers amount")
    argument_parser.add_argument(
        "-k", type=int, required=True, help="search for k frequent words"
    )
    args = argument_parser.parse_args()

    server = Master(args.w, count_top_frequent_words, args.k)
    server.run()
