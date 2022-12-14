import csv

from openpyxl import Workbook
from openpyxl.worksheet.worksheet import Worksheet

# получаем лист с данными из csv файла
with open("data.csv", "r", encoding="utf-8") as file:
    src_list = list(csv.reader(file))

# получаем лист, где каждый элемент - лист со значениями для одной строки в экселе
row_headers = [""] + [f"Person {indx}" for indx in range(1, len(src_list))]
row_id, row_name, row_phone = [], [], []

for id_, name, _, phone in src_list:
    row_id.append(id_)
    row_name.append(name)
    row_phone.append(phone)

rows = [row_headers, row_id, row_name, row_phone]

# Добавляем строки в книгу эксель и сохраняем
wb = Workbook()
sheet: Worksheet = wb.active
for row in rows:
    sheet.append(row)

wb.save("data.xlsx")
