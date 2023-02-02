#!/usr/bin/python3

import logging
import employee2

from typing import Union

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

file_handler = logging.FileHandler('test2.log')
file_handler_err = logging.FileHandler('test_error.log')
file_handler_err.setLevel(logging.ERROR)

file_handler.setFormatter(formatter)
file_handler_err.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(file_handler_err)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(stream_handler)

def add(x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
    """Add Function"""
    return x + y

def subtract(x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
    """Subtract function"""
    return x - y

def multiply(x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
    """Multiply Function"""
    return x * y

def divide(x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
    """Divide function"""
    try:
        return x / y
    except ZeroDivisionError:
        logger.exception("Can't divide by zero")
        # logger.error("Can't divide by zero")


if __name__ == "__main__":
    num_1 = 44
    num_2 = 0

    add_result = add(num_1, num_2)
    # print('Add: {} + {} = {}'.format(num_1, num_2, add_result))
    logger.debug('Add: {} + {} = {}'.format(num_1, num_2, add_result))

    sub_result = subtract(num_1, num_2)
    # print('Subtract: {} + {} + {}'.format(num_1, num_2, sub_result))
    logger.debug('Subtract: {} - {} = {}'.format(num_1, num_2, sub_result))

    mul_result = multiply(num_1, num_2)
    # print('Multiply: {} + {} + {}'.format(num_1, num_2, mul_result))
    logger.debug('Multiply: {} * {} = {}'.format(num_1, num_2, mul_result))

    div_result = divide(num_1, num_2)
    # print('Divide: {} + {} + {}'.format(num_1, num_2, div_result))
    logger.debug('Divide: {} / {} = {}'.format(num_1, num_2, div_result))