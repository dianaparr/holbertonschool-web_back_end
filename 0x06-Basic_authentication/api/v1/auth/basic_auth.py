#!/usr/bin/env python3
""" Module named basic_auth to the class Auth """


from api.v1.auth.auth import Auth
from flask import request
from typing import List, TypeVar


class BasicAuth(Auth):
    """ Class BasicAuth empty """
    pass
