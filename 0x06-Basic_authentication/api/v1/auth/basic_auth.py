#!/usr/bin/env python3
""" Module named basic_auth to the class Auth """


from api.v1.auth.auth import Auth
from flask import request
from typing import List, TypeVar


class BasicAuth(Auth):
    """ Class BasicAuth empty """
    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """ Method that return the Base64 part of the Authorization
            header for a Basic Authentication
        """
        if (authorization_header is None or
                type(authorization_header) is not str or
                not authorization_header.startswith("Basic ")):
            return None
        return authorization_header[6:]
