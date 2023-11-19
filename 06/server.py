"""
- Сервер должен поддерживать взаимодействие с любым числом клиентов;
- Мастер и воркеры это разные потоки в едином приложении сервера;
- Количество воркеров задается при запуске;
- Мастер слушает порт, на который клиенты будут по TCP отправлять урлы для обкачки;
- Мастер принимает запроc и передает его одному из воркеров;
- Воркер читает url от клиента;
- Воркер обкачивает url по http и возвращает клиенту топ K самых частых слов
  и их частоту в формате json {"word1": 10, "word2": 5};
- После каждого обработанного урла сервер должен вывести статистику:
  сколько урлов было обработано на данный момент суммарно всеми воркерами;
"""

import argparse
import threading
import requests
import json

from typing import Callable
from collections import Counter
from bs4 import BeautifulSoup


def count_top_frequent_words(url, k: int) -> dict:
    response = requests.get(url)

    soup = BeautifulSoup(response.text, features="html.parser")
    count = dict(Counter(soup.get_text().split()))

    top_frequent = dict()

    for key in sorted(count, reverse=True, key=lambda x: count[x])[:k]:
        top_frequent[key] = count[key]

    return json.dumps(top_frequent, indent=4, ensure_ascii=False)


class Master:
    def __init__(self, workers: int):
        self.workers

    def start(self):
        # init workers
        pass


class Worker(threading.Thread):
    def __init__(self, func: Callable):
        self.func = func

    def run():
        pass


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

    # server = Master(args.k)
    # server.start()

    result = count_top_frequent_words(
        "https://ru.wikipedia.org/wiki/Техническая_интеллигенция", 10
    )

    print(result)
