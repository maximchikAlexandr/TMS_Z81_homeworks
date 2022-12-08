from random import randint
from timeit import default_timer
from typing import Callable


def logging_func(func: Callable):
    def inner(*args, **kwargs):
        start_time = default_timer()
        res = func(*args, **kwargs)
        diff_time = round(default_timer() - start_time, 6)
        print(f"func '{func.__name__}', running time - {diff_time:.6f}")
        return res

    return inner


@logging_func
def max_bultin(*args) -> int:
    return max(*args)


def recursive_max(some_list: list[int], max_value: int = 0) -> int:
    """
    Your code is here
    """
    if not some_list:
        return max_value
    temp_value = some_list.pop()
    max_value = temp_value if temp_value > max_value else max_value
    return recursive_max(some_list, max_value)


@logging_func
def my_recursive_max(*args) -> int:
    return recursive_max(*args)


numbers = [randint(1, 50) for _ in range(990)]
max_bultin(numbers)
my_recursive_max(numbers)
