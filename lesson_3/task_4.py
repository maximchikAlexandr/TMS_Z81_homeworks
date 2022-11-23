n = int(input())
seq = range(1, n + 1)
result1, result2, i = 0, 0, 0

for num in seq:
    result1 += num ** 3

while i < len(seq):
    result2 += seq[i] ** 3
    i += 1

assert result1 == result2
print(result1, result2, sep='\n')
