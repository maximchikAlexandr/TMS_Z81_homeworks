while True:
    name, age = input("Введите имя:\n"), input("Введите возраст:\n")

    if not age.isdigit() or int(age) <= 0:
        print('Ошибка, повторите ввод')
        continue
    else:
        age = int(age)

    if age in range(1, 10):
        print(f"Привет, шкет {name}")
    elif age in range(10, 19):
        print(f"Как жизнь {name}")
    elif age in range(19, 100):
        print(f"Что желаете {name}")
    else:
        print(f"{name}, вы лжете - в наше время столько не живут...")
