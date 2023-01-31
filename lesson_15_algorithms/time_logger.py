from timeit import default_timer
from typing import Callable


def logging_func(func: Callable):
    def inner(*args, **kwargs):
        start_time = default_timer()
        res = func(*args, **kwargs)
        diff_time = round(default_timer() - start_time, 6)
        print(f"func '{func.__name__}', running time - {diff_time:.6f} sec")
        return res

    return inner
