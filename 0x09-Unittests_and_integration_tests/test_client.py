#!/usr/bin/env python3
""" Test module named test_client """

import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """ TestGithubOrgClient class that inherits from unittest.TestCase.
    """
    @parameterized.expand([
        "google",
        "abc"])
    @patch("client.get_json")
    def test_org(self, name_org, mock_url):
        """ Method should test that GithubOrgClient.org
            returns the correct value. """
        endpoint = "https://api.github.com/orgs/{}".format(name_org)
        get_org = GithubOrgClient(name_org)
        self.assertEqual(get_org.org, mock_url.return_value)
        mock_url.assert_called_once_with(endpoint)

    def test_public_repos_url(self):
        """ """
        mock_url = "www.someurl.com"
        the_payload = {"repos_url": mock_url}
        with patch('client.GithubOrgClient.org',
                   PropertyMock(return_value=the_payload)):
            res = GithubOrgClient("somewhere")
            self.assertEqual(res._public_repos_url, mock_url)
