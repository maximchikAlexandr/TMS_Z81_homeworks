"""
Описать Dataclass, который
- содержит три произвольных поля, разных типов
- имеет один-единственный classmethod, который проверяет типы этих трех полей и возвращает объект
Dataclass'a
- является НЕизменяемым (у объекта этого класса нельзя изменить значения атрибута/добавить
новый атрибут после его создания)
"""

from dataclasses import dataclass
from typing import Union


@dataclass(frozen=True)
class Human:
    """Human"""

    name: str
    age: int
    weight: Union[float, int]

    @classmethod
    def build(cls, name, age, weight):
        check_tuple = (
            isinstance(name, str),
            isinstance(age, int),
            isinstance(weight, Union[float, int]),
        )
        if all(check_tuple):
            return cls(name, age, weight)
        return None

    @staticmethod
    def hello_world():
        print("Hello world!")




class TestMetaClass(type):
    """TestMetaClass"""

    def __new__(cls, name, base, attrs):
        attrs.update({"hello": staticmethod(Human.hello_world)})
        return super().__new__(cls, name, base, attrs)


class TestClass(metaclass=TestMetaClass):
    """TestClass"""

    def move(self):
        print("Moove")

if __name__ == '__main__':
    test_obj = TestClass()
    test_obj.hello()
