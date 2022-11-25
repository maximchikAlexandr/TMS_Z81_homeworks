from itertools import product


list_1 = [1, 2, 3]
list_2 = [1, 2, 3, 4, 5]

result1 = [(x1, x2) for x1 in list_1 for x2 in list_2]
result2 = list(product(list_1, list_2))

assert result1 == result2
print(result1, result2, sep='\n')
