from time import sleep

from task_1 import Auto, attributes


class Truck(Auto):
    """class Truck"""

    def __init__(self, brand, age, mark, max_load, color="black", weight=1) -> None:
        super().__init__(brand, age, mark, color, weight)
        self.max_load: int = max_load

    def move(self) -> None:
        print("attention")
        super().move()

    def load(self) -> None:
        sleep(1)
        print("load")
        sleep(1)


class Car(Auto):
    """class Car"""

    def __init__(self, brand, age, mark, max_speed, color="black", weight=1) -> None:
        super().__init__(brand, age, mark, color, weight)
        self.max_speed = max_speed

    def move(self) -> None:
        super().move()
        print(f"max speed is {self.max_speed}")


# check class Truck
truck = Truck("Lada", 5, "Granta", 1)
truck.move()
for attr in attributes + ("load",):
    assert hasattr(truck, attr), f"Нет аттрибута {attr}"

# check class Car
car = Car("Lada", 5, "Granta", 120)
car.move()
for attr in attributes:
    assert hasattr(truck, attr), f"Нет аттрибута {attr}"
