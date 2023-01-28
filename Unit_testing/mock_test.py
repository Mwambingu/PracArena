#!/usr/bin/python3

import unittest
from unittest.mock import patch, MagicMock

from mock_me import add, len_joke, get_joke

class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(5, 6), 11)

class TestJoke(unittest.TestCase):
    @patch('mock_me.get_joke')
    def test_len_joke(self, mock_get_joke):
        mock_get_joke.return_value = 'one'
        self.assertEqual(len_joke(), 3)

    @patch('mock_me.requests')
    def test_get_joke(self, mock_requests):

        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'setup':'Hello World', 'delivery':'Not hello world'}
        mock_requests.get.return_value = mock_response
        self.assertEqual(get_joke(), ('Hello World', 'Not hello world'))

    @patch('mock_me.requests')
    def test_fail_get_joke(self, mock_requests):

        mock_response = MagicMock(status_code=300)
        mock_requests.get.return_value = mock_response
        self.assertEqual(get_joke(), 'No Jokes')


if __name__ == "__main__":
    unittest.main()
