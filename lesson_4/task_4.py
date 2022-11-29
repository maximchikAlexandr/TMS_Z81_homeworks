from datetime import datetime
from time import sleep


def get_my_time() -> str:
    sleep(1)
    return datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')


n = int(input('Введите целое число:\n'))
time_list = [get_my_time() for _ in range(n)]
print(f'{time_list=}')
