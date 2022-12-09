INPUT_LIST = [input() + "\n" for _ in range(4)]


def write_to_txt(lines: list[str], mode: str) -> None:
    with open("input.txt", mode, encoding="utf-8") as file:
        file.writelines(lines)


write_to_txt(INPUT_LIST[:2], "w")
write_to_txt(INPUT_LIST[2:], "a")
