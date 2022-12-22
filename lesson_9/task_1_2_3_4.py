from dataclasses import dataclass
from typing import Union


@dataclass(frozen=True)
class Human:
    '''Human'''
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


human = Human.build("John", 66, 66.0)
# human.hello_world()


class TestMetaClass(type):
    '''TestMetaClass'''
    def __new__(cls, name, base, attrs):
        attrs.update({'hello': staticmethod(Human.hello_world) })
        return super().__new__(cls, name, base, attrs)


class TestClass(metaclass=TestMetaClass):
    '''TestClass'''
    def move(self):
        print('Moove')

test_obj = TestClass()
test_obj.hello()
