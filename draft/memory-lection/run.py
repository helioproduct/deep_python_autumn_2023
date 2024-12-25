from memory_profiler import profile


@profile
def some_func():
    lst1 = []
    lst2 = "1" * 1000


some_func()
