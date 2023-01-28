#!/usr/bin/python3

import unittest
from unittest.mock import patch, MagicMock
from calc import add, subtract, multiply, divide, calc


class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(3, 4), 7)

    def test_subtract(self):
        self.assertEqual(subtract(3, 4), -1)

    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)

    def test_divide(self):
        self.assertEqual(divide(3, 4), 0.75)
        self.assertEqual(divide(2, 0), 'Can\'t divide by 0!')

    @patch('calc.add')
    def test_add_calc(self, mock_add):
        print(mock_add.__dict__)
        self.assertEqual(calc(1, 3, 5), 8)


if __name__ == '__main__':
    unittest.main()
