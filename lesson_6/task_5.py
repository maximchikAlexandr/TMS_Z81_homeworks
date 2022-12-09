import csv

from openpyxl import Workbook
from openpyxl.worksheet.worksheet import Worksheet

# получаем лист с данными из csv файла
with open("data.csv", "r", encoding="utf-8") as file:
    src_list = list(csv.reader(file))

# получаем лист, где каждый элемент - лист со значениями для одной строки в экселе
row_headers = [""] + [f"Person {indx}" for indx in range(1, len(src_list))]


def filter_list_by_indx(source: list[list[str]], indx: int) -> list[str]:
    return [elem[indx] for elem in source]


row_id = filter_list_by_indx(src_list, indx=0)
row_name = filter_list_by_indx(src_list, indx=1)
row_phone = filter_list_by_indx(src_list, indx=3)
rows = [row_headers, row_id, row_name, row_phone]

# Добавляем строки в книгу эксель и сохраняем
wb = Workbook()
sheet: Worksheet = wb.active
for row in rows:
    sheet.append(row)

wb.save("data.xlsx")
