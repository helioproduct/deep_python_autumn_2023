import json
import time


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
