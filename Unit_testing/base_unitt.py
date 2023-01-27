#!/usr/bin/python3

import unittest
from test_task import add, subtract, multiply, is_int

class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])

        with self.assertRaises(TypeError):
            s.split(2)

class TestFunctions(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(3,2), 5)
        with self.assertRaises(TypeError):
            add(4, "Hello")

    def test_subtract(self):
        self.assertEqual(subtract(5,3), 2)

    def test_multiply(self):
        self.assertEqual(multiply(5, 6), 30)

    def test_is_int(self):
        self.assertTrue(is_int("1"))
        self.assertTrue(is_int(5))
        self.assertFalse(is_int("Hello"))

if __name__ == '__main__':
    unittest.main()
