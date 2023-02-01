#!/usr/bin/python3
# Logging Levels
# DEBUG: Detalied infromation, typically of interest only when diagnosing problems.

# INFO: Confirmation that things are working as expected.

# WARNING: An indication that something unexpected happened, or indicative of some problem in the near future (e.g. 'disk space low'). The software is still working as expected.

# ERROR: Due to a more serious problem, the software has not been able to perform some function.

# CRTITICAL: A serious error, indicationg that the program itself may be unable to continue running.

import logging

from typing import Union

logging.basicConfig(filename='test.log', level=logging.DEBUG,
format='%(asctime)s:%(levelname)s:%(message)s')

def add(x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
    """Add Fucntion"""
    return x + y

def subtract(x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
    """Subtract function"""
    return x - y

def multiply(x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
    """Multiply Function"""
    return x * y

def divide(x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
    """Divide function"""
    return x / y


if __name__ == "__main__":
    num_1 = 44
    num_2 = 33

    add_result = add(num_1, num_2)
    # print('Add: {} + {} = {}'.format(num_1, num_2, add_result))
    logging.debug('Add: {} + {} = {}'.format(num_1, num_2, add_result))

    sub_result = subtract(num_1, num_2)
    # print('Subtract: {} + {} + {}'.format(num_1, num_2, sub_result))
    logging.debug('Subtract: {} + {} + {}'.format(num_1, num_2, sub_result))

    mul_result = multiply(num_1, num_2)
    # print('Multiply: {} + {} + {}'.format(num_1, num_2, mul_result))
    logging.debug('Multiply: {} + {} + {}'.format(num_1, num_2, mul_result))

    div_result = divide(num_1, num_2)
    # print('Divide: {} + {} + {}'.format(num_1, num_2, div_result))
    logging.debug('Divide: {} + {} + {}'.format(num_1, num_2, div_result))