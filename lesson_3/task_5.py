original_num = 2

while True:
    user_num = input("Введите число:\n")
    if user_num.isdigit():
        user_num = int(user_num)
    else:
        continue

    if original_num == user_num:
        print('Угадали!')
        break
    else:
        print('Не угадали!')
