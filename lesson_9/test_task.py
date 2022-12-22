from dataclasses import FrozenInstanceError
from task_1_2_3_4 import Human

human = Human.build("John", 66, 66.0)

# Проверяем неизменяемость
name, age, weight = human.name, human.age, human.weight


try:
    human.name, human.age, human.weight = 'Mary', 25, 50.0
except FrozenInstanceError:
    pass
else:
    print('Класс должен быть неизменяемым!')

assert name == human.name, f"{name} != {human.name} "
assert age == human.age, f"{age} != {human.age} "
assert weight == human.weight, f"{weight} != {human.weight} "
