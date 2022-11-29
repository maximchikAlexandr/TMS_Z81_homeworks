from math import factorial


def fact(num):
    if num == 1:
        return 1
    else:
        return num * fact(num - 1)


n = int(input('Введите целое число:\n'))
assert fact(n) == factorial(n)
print(f'{fact(n)=}')
