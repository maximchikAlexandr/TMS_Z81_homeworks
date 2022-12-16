class Point:
    """class Point"""



class Circle:
    """class Circle"""

    def __init__(self, radius: int) -> None:
        self.radius = radius

    def __sub__(self, other):
        if isinstance(other, Circle):
            diff = abs(other.radius - self.radius)
            if diff:
                return self.__class__(diff)
            return Point()


res1 = Circle(5) - Circle(2)
assert isinstance(res1, Circle)
assert res1.radius == 3

res2 = Circle(5) - Circle(5)
assert isinstance(res2, Point)
