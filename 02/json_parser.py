import json
import time
from typing import Callable


def mean(k):
    execution_times = []

    def timer(func):
        def wrapper(*args, **kwargs):
            start_ts = time.time()
            res = func(*args, **kwargs)
            end_ts = time.time()

            execution_times.append(end_ts - start_ts)
            if len(execution_times) > k:
                execution_times.pop(0)

            average_time = sum(execution_times) / len(execution_times)
            print(f"mean time of last {len(execution_times)} calls = {average_time}")
            return res

        return wrapper

    return timer


def parse_json(
    json_str: str, keyword_callback: Callable, required_fields=None, keywords=None
) -> bool:
    if keyword_callback is None or required_fields is None or keywords is None:
        return False

    json_doc = json.loads(json_str)

    for key in required_fields:
        if key in json_doc:
            for keyword in keywords:
                if keyword in json_doc(key).split():
                    keyword_callback(key, keyword)
    return True
