class Auto:
    '''Class auto'''
    def __init__(
            self, brand: str, age: int, mark: str, color: str = "black", weight: int = 1
    ) -> None:
        self.brand = brand
        self.age = age
        self.color = color
        self.mark = mark
        self.weight = weight

    def move(self) -> None:
        print("move")

    def stop(self) -> None:
        print("stop")

    def birthday(self) -> None:
        self.age += 1


auto = Auto("Lada", 5, "Granta")

attributes = ("brand", "age", "mark", "color", "weight", "move", "stop", "birthday")
for attr in attributes:
    assert hasattr(auto, attr), f"Нет аттрибута {attr}"
