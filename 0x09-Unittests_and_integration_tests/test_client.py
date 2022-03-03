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
        """ Method to unit-test GithubOrgClient._public_repos_url """
        mock_url = "www.someurl.com"
        the_payload = {"repos_url": mock_url}
        with patch('client.GithubOrgClient.org',
                   PropertyMock(return_value=the_payload)):
            res = GithubOrgClient("somewhere")
            self.assertEqual(res._public_repos_url, mock_url)

    @patch("client.get_json")
    def test_public_repos(self, repo_mock):
        """ To unit-test GithubOrgClient.public_repos. """
        the_payload = [{"name": "someone"}, {"name": "Betty"}]
        repo_mock.return_value = the_payload
        with patch("client.GithubOrgClient._public_repos_url",
                   new_callable=PropertyMock) as mock_client:
            test_name = GithubOrgClient("someone").public_repos()
            self.assertEqual(test_name, ['someone', 'Betty'])
            mock_client.assert_called_once()
            repo_mock.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, key, expected_return):
        """ To unit-test GithubOrgClient.has_license. """
        self.assertEqual(
            GithubOrgClient.has_license(repo, key), expected_return)
