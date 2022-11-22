dict_case = {
    (1, 11) : "Привет {name}",
    (11, 19) : "Привет {name}",
    (19, 100) : "Привет {name}",
    (100, 1000) : "Привет {name}"
}

while True:
    name, age = input("Введите имя:\n"), input("Введите возраст:\n")

    if not age.isdigit() or int(age) <= 0:
        print('Ошибка, повторите ввод')
        continue
    else:
        age = int(age)

    if age in range(1, 11):
        print(f"Привет {name}")
    elif age in range(11, 19):
        print(f"Привет {name}")
    elif age in range(19, 100):
        print(f"Привет {name}")
    else:
        print(f"Привет {name}")
