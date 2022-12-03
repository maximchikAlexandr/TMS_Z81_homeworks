from math import factorial


def fact(number: int) -> int:
    if number == 1:
        return 1
    return number * fact(number - 1)


num = int(input("Введите целое число:\n"))
assert fact(num) == factorial(num), f"Неверное значение {fact(num)=}, а должно быть {factorial(num)}"
print(f"{fact(num)=}")
