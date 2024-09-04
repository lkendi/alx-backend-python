#!/usr/bin/env python3
"""
Unittest module
"""
import unittest.mock
from parameterized import parameterized
import unittest
from unittest.mock import Mock, patch
from utils import access_nested_map
from utils import get_json


class TestAccessNestedMap (unittest.TestCase):
    """
    TestAccessNestedMap class:
        Contains unittests for the access_nested_map function
    """

    @parameterized.expand([
        ({'a': '1'}, ('a',), '1'),
        ({'a': {'b': '2'}}, ('a',), {'b': '2'}),
        ({'a': {'b': '2'}}, ('a', 'b'), '2'),
    ])
    def test_access_nested_map(self, input_map, path, expected_val):
        """
        Tests the access_nested_map function with various input maps and paths.

        Parameters:
            input_map (dict): The input dictionary to be accessed.
            path (tuple): A tuple of keys representing the path to the value.
            expected_val: The expected value at the given path.

        Returns:
            None
        """
        self.assertEqual(access_nested_map(input_map, path), expected_val)

    @parameterized.expand([
        ({}, ('a',)),
        ({'a': '1'}, ('a', 'b')),
    ])
    def test_access_nested_map_exception(self, input_map, path):
        """
        Tests the access_nested_map function with various input maps and paths
        that result in KeyErrors.

        Parameters:
            input_map (dict): The input dictionary to be accessed.
            path (tuple): A tuple of keys representing the path to the value.

        Returns:
            None
        """
        with self.assertRaises(KeyError):
            access_nested_map(input_map, path)


class TestGetJson(unittest.TestCase):
    """TestGetJson class:
        Contains unittests for the get_json function
    """

    @parameterized.expand([
        ("https://example.com", {"payload": True}),
        ("https://holberton.io", {"payload": False}),
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """
        Tests that the utils.get_json function
        returns the expected result
        """

        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        result = get_json(test_url)
        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)


if __name__ == "__main__":
    unittest.main()
