from typing import Iterable


def get_geometric_progression(base_num: int, multiplier: int, count_elements: int) -> Iterable:
    current_element = base_num
    for _ in range(count_elements):
        current_element *= multiplier
        yield current_element


geometric_progression = get_geometric_progression(base_num=2, multiplier=2, count_elements=8)

for elem in geometric_progression:
    print(elem)
