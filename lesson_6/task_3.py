import json


sourse_dict = {
    1000000: ("Mike", 25),
    2000000: ("Nick", 26),
    3000000: ("John", 27),
    4000000: ("Sam", 28),
    5000000: ("Kevin", 29)
}
with open("data.json", "w", encoding="utf-8") as file:
    json_str = json.dumps(sourse_dict)
    json.dump(json_str, file)
