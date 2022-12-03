from collections import Counter
from random import randint


def my_counter(lst: list[int]) -> dict[int, int]:
    res: dict[int, int] = {}
    for elem in lst:
        res[elem] = res.get(elem, 0) + 1
    return res


numbers = [randint(1, 10) for _ in range(100)]
result = my_counter(numbers)
assert result == Counter(numbers), f'Неверное значение {result=}, а должно быть {Counter(numbers)}'
print(f'{result=}')
