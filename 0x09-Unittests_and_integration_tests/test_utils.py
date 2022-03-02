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

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b')])
    def test_access_nested_map_exception(self, nested_map, path, expected_err):
        """ Method to test that the method returns the access
            nested map with key path. Use the assertRaises context manager
            to test that a KeyError is raised. Param expand example:

            Traceback (most recent call last):
                File "<stdin>", line 1, in <module>
                File "<stdin>", line 4, in access_nested_map
            KeyError: 'b'
        """
        with self.assertRaises(KeyError) as key_err:
            access_nested_map(nested_map, path)
            the_exception = key_err.exception
            self.assertEqual(expected_err, the_exception)
