from random import randint
from timeit import default_timer


from lesson_4.homework_task2 import recursive_max


def logging_func(func):
    def inner(*args, **kwargs):
        start_time = default_timer()
        res = func(*args, **kwargs)
        diff_time = round(default_timer() - start_time, 6)
        print(f"func '{func.__name__}', running time - {diff_time:.6f}")
        return res

    return inner


numbers = [randint(1, 50) for _ in range(990)]


@logging_func
def max_bultin(*args) -> int:
    return max(*args)


@logging_func
def recursive_max_import(*args) -> int:
    return recursive_max(*args)


max_bultin(numbers)
recursive_max_import(numbers)
