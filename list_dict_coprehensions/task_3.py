my_list = list(range(1, 101))
result = [elem * 10 if elem % 4 else elem * 2 for elem in my_list if not elem % 10]

print(result)
