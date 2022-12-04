"""
1. Написать рекурсивную функцию, которая принимает на вход Список со следующей структурой:

-- Список может содержать числа и/или вложенные списки
-- вложенные списки повторяют структуру родительского списка (содержат числа и/или вложенные списки)
-- уровень вложенности не определен

Функция должна возвращать новый список, который будет содержать все элементы из входного списка и
вложенных в него списков (на одном уровне)

Примеры входных списков:
"""


def recursive_flat(source_list: list | int, output_list: list[int] | None = None):
    """
    Your code is here
    """
    if output_list is None:
        output_list = []
    if isinstance(source_list, list):
        for elem in source_list:
            recursive_flat(elem, output_list)
    elif isinstance(source_list, int):
        output_list.append(source_list)
    return output_list


# Пример
source_list_1 = [[1, 2], [3, 4], [5, 6]]
print(source_list_1)
assert recursive_flat(source_list_1) == [1, 2, 3, 4, 5, 6]

source_list_2 = [1, [2, 3], [4, 5, [6]], [7, 8], 9, 10]
print(source_list_2)
assert recursive_flat(source_list_2) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

source_list_3 = [[1, 2], [3, 4, [5, 6]], [7, 8, [9, 10, [11, 12]]]]
print(source_list_3)
assert recursive_flat(source_list_3) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# ПРИМЕЧАНИЕ:
# Помните, что списки поддерживают слияние через метаметический оператор +
#
# merged = [1, 2, 3] + [3, 4, 5]
# >> [1, 2, 3, 3, 4, 5,]
