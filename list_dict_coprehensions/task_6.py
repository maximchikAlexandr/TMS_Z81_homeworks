dict_1 = {
  "key1": 1,
  "key2": 2,
  "key3": 3,
  "key4": 4,
  "key5": 5
}

dict_2 = {val: key for key, val in dict_1.items()}

assert tuple(dict_1.keys()) == tuple(dict_2.values())
assert tuple(dict_2.keys()) == tuple(dict_1.values())
print(dict_2)
