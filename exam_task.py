"""
Написать декоратор, который считает и выводит среднее время выполнения последних k вызовов исходной функции.
k задается через параметр декоратора.
После каждого вызова задекорированной функции должно выводиться среднее по k последним вызовам.
Использование памяти - O(n)
"""

from time import time
from collections import deque


def mean_deco(k):

    times = deque()
    sm = 0

    def timer(func):
        def inner(*args, **kwargs):
            start_time = time()
            result = func(*args, **kwargs)
            times.append(time() - start_time)
            sm += time() - start_time
            print(f"Average exec time is {sm / len(times)}")
            if len(times) > k:
                times.popleft()
                # print("popleft")
            return result

        return inner

    return timer


# @mean_deco(2)
def test():
    return 2**128


timer = mean_deco(2)
test = timer(test)

test()
test()
test()
