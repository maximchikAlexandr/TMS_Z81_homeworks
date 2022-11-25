my_list = list(range(1, 51))
my_new_list = [my_list[-i-1] for i in range(len(my_list))]

assert my_list[::-1] == my_new_list
print(my_new_list)
