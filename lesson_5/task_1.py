from random import randint

numbers = [randint(1, 50) for _ in range(10)]
check_even = lambda x: print("нечетное" if x % 2 else "четное")

for number in numbers:
    print(number, end=" - ")
    check_even(number)
