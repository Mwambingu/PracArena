#!/usr/bin/python3

from typing import Union

def add(num1: int, num2:int ) -> int:
    if type(num1) != int or type(num2) != int:
        raise TypeError("You have entered an a value that's not an integer!")
    return num1 + num2

def subtract(num1: int, num2:int ) -> int:
    return num1 - num2

def multiply(num1: int, num2:int ) -> int:
    return num1 * num2

def is_int(num: Union[str, int]) -> bool:
    if type(num) == int:
        return True
    if num.isdigit():
        return True
    return False
