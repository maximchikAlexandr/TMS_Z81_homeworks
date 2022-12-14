import csv
import json

with open("data.json", "r", encoding="utf-8") as file:
    json_str = json.load(file)
    src_dict = json.loads(json_str)

phones = ["098-98-51", "098-98-52", "098-98-53", "098-98-54", "098-98-55"]
src_list = []

for (id_, (name, age)), phone in zip(src_dict.items(), phones):
    src_list.append(
        {
            "id": id_,
            "name": name,
            "age": age,
            "phone": phone,
        }
    )

with open("data.csv", "w", encoding="utf-8") as file:
    csv_writer = csv.DictWriter(file, fieldnames=src_list[0])
    csv_writer.writeheader()
    csv_writer.writerows(rowdicts=src_list)
