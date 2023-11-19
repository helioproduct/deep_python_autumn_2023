import argparse
import json
import socket
import threading

from typing import Callable
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup

import requests


def count_top_frequent_words(url, k: int) -> dict:
    response = requests.get(url)

    soup = BeautifulSoup(response.text, features="html.parser")
    count = dict(Counter(soup.get_text().split()))

    top_frequent = {}

    for key in sorted(count, reverse=True, key=lambda x: count[x])[:k]:
        top_frequent[key] = count[key]

    return json.dumps(top_frequent, indent=4, ensure_ascii=False)


class Master(threading.Thread):
    # start workers
    def __init__(self, workers_amount: int, func: Callable):
        super(Master, self).__init__()

        self.workers_amount = workers_amount
        self.func = func

        # endpoint for recieving all requests
        self.serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
        self.serv_sock.bind(("127.0.0.1", 53210))
        self.serv_sock.listen(10)

        self.executor = ThreadPoolExecutor(max_workers=workers_amount)

    def run(self):
        while True:
            client_sock, addr = self.serv_sock.accept()

            while True:
                data = client_sock.recv(1024)
                if not data:
                    break

                url = data.decode()
                print(url)
                client_sock.sendall("fuck you motherfucker".encode())

            client_sock.close()


if __name__ == "__main__":
    argument_parser = argparse.ArgumentParser(
        "Server", "Multithreading app for scraping url for getting top K frequent words"
    )
    argument_parser.add_argument(
        "-w", default=None, type=int, help="workers amount", required=True
    )
    argument_parser.add_argument(
        "-k", default=None, type=int, help="search for k frequent words", required=True
    )

    # args = argument_parser.parse_args()

    server = Master(10, count_top_frequent_words)
    server.start()
