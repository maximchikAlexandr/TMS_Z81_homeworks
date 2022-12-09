import csv
import json

with open("data.json", "r", encoding="utf-8") as file:
    json_str = json.load(file)
    src_dict = json.loads(json_str)

phones = ["098-98-51", "098-98-52", "098-98-53", "098-98-54", "098-98-55"]
src_list = []

for id_, name_and_age, phone in zip(src_dict.keys(), src_dict.values(), phones):
    src_list.append(
        {
            "id": id_,
            "name": name_and_age[0],
            "age": name_and_age[1],
            "phone": phone,
        }
    )

with open("data.csv", "w", encoding="utf-8") as file:
    csv_writer = csv.DictWriter(file, fieldnames=src_list[0])
    csv_writer.writeheader()
    csv_writer.writerows(rowdicts=src_list)
