#!/usr/bin/env python3
""" Module named auth to the class Auth """


from flask import request
from typing import List, TypeVar


class Auth():
    """Class to manage the API authentication """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ public method that return false """
        return False

    def authorization_header(self, request=None) -> str:
        """ Public method that return None.

            Args:
                request -> will be the Flask request object.
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Public method that return None.

            Args:
                request -> will be the Flask request object.
        """
        return None
