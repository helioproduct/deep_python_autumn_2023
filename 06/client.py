import socket
import argparse
import json

from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urlparse


TCP_ADRESS = "127.0.0.1"
PORT = 53210


def make_request(url: str):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((TCP_ADRESS, PORT))
        s.sendall(url.encode())
        answer = s.recv(1024)
    return answer


def read_file(filename: str):
    with open(filename) as file:
        lines = [line.rstrip() for line in file]
    return lines


def simplify_url(url):
    parsed_url = urlparse(url)
    domain_parts = parsed_url.netloc.split(".")
    # Проверяем, есть ли поддомен (например, 'www')
    if len(domain_parts) > 2:
        # Возвращаем последние две части (домен второго уровня)
        return ".".join(domain_parts[-2:])
    else:
        # Если нет поддомена, возвращаем всё, что есть
        return parsed_url.netloc


if __name__ == "__main__":
    argument_parser = argparse.ArgumentParser(
        "Client", "Multithreading app for sending url to server, recieving answer"
    )
    argument_parser.add_argument("threads_count", default=None, type=int)
    argument_parser.add_argument("urls_file", default=None, type=str)

    args = argument_parser.parse_args()
    urls = read_file(args.urls_file)

    thread_pool = ThreadPoolExecutor(max_workers=args.threads_count)

    for url in urls:
        work = thread_pool.submit(make_request, url)
        json_answer = json.loads(work.result())
        print(simplify_url(url), json_answer)
