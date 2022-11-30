from collections import Counter
from random import randint


def my_counter(lst: list) -> dict:
    res = {}
    for elem in lst:
        if res.get(elem):
            res[elem] += 1
        else:
            res[elem] = 1
    return res


numbers = [randint(1, 10) for _ in range(100)]
result = my_counter(numbers)
assert result == Counter(numbers)
print(f'{result=}')
