"""
Написать рекурсивную функцию, которая принимат на вход список целых чисел
и возвращает максимальное число в списке
"""


def recursive_max(some_list: list[int], max_value: int = 0) -> int:
    """
    Your code is here
    """
    if not some_list:
        return max_value
    temp_value = some_list.pop()
    max_value = temp_value if temp_value > max_value else max_value
    return recursive_max(some_list, max_value)


# Test
source = [2, 1, 0, 5, 7, 6, 4, 3]
print(source)
assert recursive_max(source) == 7
