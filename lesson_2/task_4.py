input_str = input().strip()
even, uneven = input_str[1::2], input_str[::2]
print(f'Введена строка {input_str}', end='\n' * 2)
print(even, uneven, sep=' ' * 5, end='\n!!!')
