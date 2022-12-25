from datetime import datetime
from logging import DEBUG, basicConfig, exception
from operator import add, mul, sub, truediv
from traceback import print_exception
from typing import Callable, Dict, Union

Number = Union[int, float]
LOG_FILENAME = "logging_example.out"
basicConfig(filename=LOG_FILENAME, level=DEBUG)


class NumberTypeError(Exception):
    """My exception"""


class Calculator:
    """class Calculator"""

    operators: Dict[str, Callable] = {
        "+": add,
        "-": sub,
        "*": mul,
        "/": truediv,
    }

    @classmethod
    def calculate(cls, num1: Number, num2: Number, operator: str) -> None:
        if isinstance(num1, (float, int)) and isinstance(num2, (float, int)):
            print(cls.operators.get(operator)(num1, num2))
        else:
            raise NumberTypeError("Invalid number type")


try:
    Calculator.calculate(6, 4, "+")
except NumberTypeError as err:
    print_exception(err)
    exception(datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
