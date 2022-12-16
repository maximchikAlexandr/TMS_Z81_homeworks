class Auto:
    """Class auto"""

    def __init__(self, brand, age, mark, color="black", weight=1) -> None:
        self.brand: str = brand
        self.age: int = age
        self.color: str = color
        self.mark: str = mark
        self.weight: int = weight

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
