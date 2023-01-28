#!/usr/bin/python3

from typing import Union

def add(a: Union[int, float] , b: Union[int, float]) -> Union[int, float]:
    return a + b

def subtract(a: Union[int, float] , b: Union[int, float]) -> Union[int, float]:
    return a - b

def multiply(a: Union[int, float] , b: Union[int, float]) -> Union[int, float]:
    return a * b

def divide(a: Union[int, float] , b: Union[int, float]) -> Union[int, float]:
    try:
        return a / b
    except ZeroDivisionError:
        return "Can't divide by 0!"

def calc(selection: Union[str, int] , a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    operations = [add, subtract, multiply, divide]
    if selection:
        try:
            op = operations[selection - 1]
            return op(a, b)
        except IndexError:
            return "Incorrect selection! The selection does not exist!"
        except TypeError:
            return "Error! Selection must be an integer. a or b must be an integer or float. Check for corrections"

if __name__ == '__main__':

    value = calc(1, 3, 'jelly')
    if value:
        print(value)

    value = calc(14, 3, 7)
    if value:
        print(value)

    value = calc(1, 3, 4)
    if value:
        print(value)

    value = calc(2, 3, 4)
    if value:
        print(value)

    value = calc(3, 3, 4)
    if value:
        print(value)

    value = calc(4, 3, 4)
    if value:
        print(value)

    value = calc(4, 3, 0)
    if value:
        print(value)

