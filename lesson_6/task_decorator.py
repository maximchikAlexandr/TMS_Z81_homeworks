from functools import wraps
from typing import Callable


def list_decorator(check_num: Callable) -> Callable:
    def _list_decorator(func: Callable) -> Callable:
        @wraps(func)
        def inner(*args, **kwargs):
            numbers = func(*args, **kwargs)
            numbers = [
                num for num in numbers if check_num(num)
            ]  # modify list as you wish
            return numbers

        return inner

    return _list_decorator


def is_valid_number(num: int) -> bool:
    return not num % 11


@list_decorator(is_valid_number)
def create_list(count: int) -> list[int]:
    return list(range(1, count + 1))


result = create_list(100)
print(result)
