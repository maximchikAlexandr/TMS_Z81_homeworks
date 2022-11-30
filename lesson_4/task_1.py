def reverse_dict(target: dict[str, int]) -> dict[int, str]:
    return {val: key for key, val in target.items()}


dict_1 = {
    "key1": 1,
    "key2": 2,
    "key3": 3,
    "key4": 4,
    "key5": 5
}

print(reverse_dict(dict_1))
