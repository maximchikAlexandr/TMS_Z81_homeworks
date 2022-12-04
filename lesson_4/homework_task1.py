"""
Написать рекурсивную функцию, которая будет принимать на вход список целых чисел
и возвращать инвертированную копию этого списка (рекурсивная реализация функции reverse)
"""


def recursive_reverse(
    source_list: list[int], output_list: list[int] | None = None
) -> list[int]:
    """
    Your code is here
    """
    if output_list is None:
        output_list = []
    if not source_list:
        return output_list
    output_list.append(source_list.pop())
    return recursive_reverse(source_list, output_list)


# Test
source = [1, 2, 3, 4, 5]
print(source)
assert recursive_reverse(source) == [5, 4, 3, 2, 1]
