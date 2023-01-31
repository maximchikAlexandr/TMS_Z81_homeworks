from random import choice, randint

from time_logger import logging_func


@logging_func
def binary_searching(lst, item):
    left, right = 0, len(lst)
    while left <= right:
        mid = (right + left) // 2
        if lst[mid] == item:
            return mid
        if lst[mid] > item:
            right = mid - 1
        else:
            left = mid + 1


@logging_func
def bultin_searching(lst, item):
    return lst.index(item)


target_lst = sorted({randint(1, 10**6) for _ in range(1, 10**6, randint(1, 5))})
target_item = choice(target_lst)

print(f"Количество элементов в списке:\n{len(target_lst)}\nИскомое значение:\n{target_item}\n")
bin_res = binary_searching(target_lst, target_item)
bultin_res = bultin_searching(target_lst, target_item)

assert bin_res == bultin_res
