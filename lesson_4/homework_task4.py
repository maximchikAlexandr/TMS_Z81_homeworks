"""
Изменить реализацию функции рекурсивного поиска элемента в словаре (из предыдущего задания)
следующим образом:
- функция должна находить ПЕРВОЕ соответствие имени и возвращать результат в виде словаря:

    {'val': found_value, 'parent': found_value_parent, 'deep': found_value_deep}

"""


def recursive_search(
    target: dict | list | str,
    pattern: str,
    deep: int = -1,
    parent: str | None = None,
) -> None:
    """Your code is here"""
    found = []
    if target == pattern:
        found.append({"val": pattern, "parent": parent, "deep": deep})
    elif isinstance(target, dict):
        deep += 1
        for key, value in target.items():
            found.extend(recursive_search(value, pattern, deep, key))
    elif isinstance(target, list):
        for elem in target:
            found.extend(recursive_search(elem, pattern, deep, parent))
    return found


# Source dict
def get_source_dict():
    return {
        "key1": "John",  # deep 0
        "key2": {
            "key3": "Alex",  # deep 1
            "key4": {
                "key5": ["Kate", "Mary"],  # deep 2
                "key6": {
                    "key7": [
                        "Bob",  # deep 3
                        "Duke",
                        {
                            "key8": {  # deep 4
                                "key9": [  # deep 5
                                    "Lisa",
                                    {"key10": ["Mark"]},  # deep 6
                                ]
                            }
                        },
                    ]
                },
            },
            "key8": "Robert",  # deep 1
        },
    }


# Test
source_dict = get_source_dict()
values = [
    ("Alex", {"val": "Alex", "parent": "key3", "deep": 1}),
    ("Mary", {"val": "Mary", "parent": "key5", "deep": 2}),
    ("Duke", {"val": "Duke", "parent": "key7", "deep": 3}),
    ("Mark", {"val": "Mark", "parent": "key10", "deep": 6}),
]

for lookup_value, expected_result in values:
    RESULT = recursive_search(source_dict, lookup_value)[0]
    assert RESULT == expected_result, f"{RESULT} != {expected_result}"
