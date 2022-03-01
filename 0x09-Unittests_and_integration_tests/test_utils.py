#!/usr/bin/env python3
""" Test module named test_utils """

import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """ TestAccessNestedMap class that inherits from unittest.TestCase.

        @parameterized.expand can be used to generate test methods in
        situations where test generators cannot be used (for example,
        when the test class is a subclass of unittest.TestCase).

            src: https://pypi.org/project/parameterized/
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)])
    def test_access_nested_map(self, nested_map, path, expected):
        """ Method to test that the method returns the access
            nested map with key path """
        self.assertEqual(access_nested_map(nested_map, path), expected)
