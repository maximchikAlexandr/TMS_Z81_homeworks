# Ввести с клавиатуры целое число n. Получить сумму кубов всех целых чисел от 1 до
# n включая n). Реализовать в 2-х вариантах: используя цикл while и цикл for

n = int(input())
seq = range(1, n + 1)
result1, result2 = 0, 0


for num in seq:
    result1 += num ** 3

i = 0

while i < len(seq):
    result2 += seq[i] ** 3
    i += 1

assert result1 == result2
print(result1, result2)
