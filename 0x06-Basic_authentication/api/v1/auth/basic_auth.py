#!/usr/bin/env python3
""" Module named basic_auth to the class Auth """


from api.v1.auth.auth import Auth
from models.user import User
from typing import TypeVar
from base64 import b64decode


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

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """  Method in the class BasicAuth that returns the decoded value
            of a Base64 string base64_authorization_header
        """
        if (base64_authorization_header is None or
                type(base64_authorization_header) is not str):
            return None
        try:
            return b64decode(base64_authorization_header).decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str
                                 ) -> (str, str):
        """ Method in the class BasicAuth that returns the user email and
            password from the Base64 decoded value.
        """
        if (decoded_base64_authorization_header is None or
                type(decoded_base64_authorization_header) is not str or
                ':' not in decoded_base64_authorization_header):
            return None, None
        values_auth = decoded_base64_authorization_header.split(':', 1)
        return values_auth[0], values_auth[1]

    def user_object_from_credentials(self,
                                     user_email: str, user_pwd: str
                                     ) -> TypeVar('User'):
        """ Method in the class BasicAuth that returns the User instance based
            on his email and password.
        """
        if (user_email is None or type(user_email) is not str):
            return None
        if (user_pwd is None or type(user_pwd) is not str):
            return None
        try:
            user_found = User.search({'email': user_email})
        except Exception:
            return None
        # if user_pwd is not the password of the User instance found -> None
        for user in user_found:
            if user.is_valid_password(user_pwd):
                return user
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Method in the class BasicAuth that overloads Auth and
            retrieves the User instance for a request.
        """
        try:
            header_req = self.authorization_header(request)
            extractbase64 = self.extract_base64_authorization_header(
                header_req)
            decodebase64 = self.decode_base64_authorization_header(
                extractbase64)
            values_auth = self.extract_user_credentials(decodebase64)
            user = self.user_object_from_credentials(values_auth[0],
                                                     values_auth[1])
            return user
        except Exception:
            return None
