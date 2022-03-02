#!/usr/bin/env python3
""" Test module named test_utils """

import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch, Mock


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


class TestGetJson(unittest.TestCase):
    """ TestGetJson class that inherits from unittest.TestCase.
    """
    @parameterized.expand([
        "http://example.com", {"payload": True},
        "http://holberton.io", {"payload": False}])
    @patch('utils.get_json')
    def test_get_json(self, test_url, test_payload):
        """ Method to test that utils.get_json returns
            the expected result
        """
        # configure the value returned by calling the mock with Mock class:
        mock_cls = Mock()
        mock_cls.json.return_value = test_payload
        with patch('requests.get', return_value=mock_cls):
            res = get_json(test_url)
            # Test that the mocked get method was called exactly once
            # (per input) with test_url as argument.
            mock_cls.json.assert_called_once()
            # Test that the output of get_json is equal to test_payload.
            self.assertEqual(res, test_payload)


class TestMemoize(unittest.TestCase):
    """ TestMemoize(unittest.TestCase) class with a test_memoize method

        More about memoization and decorators:
            https://python-course.eu/advanced-python/memoization-decorators.php
    """
    def test_memoize(self):
        """ Method to test memoize """
        class TestClass:
            """ class test """

            def a_method(self):
                """ a method test """
                return 42

            @memoize
            def a_property(self):
                """ other method test """
                return self.a_method()

        with patch.object(TestClass,
                          'a_method', return_value=42) as mock_method:
            product_cls = TestClass()
            product_cls.a_property
            product_cls.a_property
            mock_method.assert_called_once()
