def check_number(num: str) -> str:
    num_temp = num[1:] if num[0] == "-" else num
    num_temp = num_temp.replace(".", "")
    if not num_temp.isdigit():
        return f"Вы ввели не корректное число: {num}"

    try:
        num = int(num)
        int_or_float = "целое"
    except ValueError:
        num = float(num)
        int_or_float = "дробное"

    if num == 0:
        return "Вы ввели 0"

    pos_or_neg = "положительное" if num > 0 else "отрицательное"

    return f"Вы ввели {pos_or_neg} {int_or_float} число: {num}"


test_list = ("-6.7", "5", "5.4r", "-.777", "0")

for elem in test_list:
    print(check_number(elem))
