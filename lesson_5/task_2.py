from random import randint

numbers = [randint(1, 50) for _ in range(10)]
str_numbers = list(map(str, numbers))

print(str_numbers)

for elem in str_numbers:
    assert isinstance(elem, str)
