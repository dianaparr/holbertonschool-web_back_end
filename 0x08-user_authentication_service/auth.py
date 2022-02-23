#!/usr/bin/env python3
""" Module called auth """


import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> str:
    """ Method that takes in a password string arguments and returns bytes. """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ Take mandatory email and password string arguments and
            return a User object.
        """
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f'User {email} already exists')
        except NoResultFound:
            user = self._db.add_user(email, _hash_password(password))
            return user

    def valid_login(self, email: str, password: str) -> bool:
        """ Try locating the user by email. If it exists, check the password
            with bcrypt.checkpw. If it matches return True. In any other
            case, return False.
        """
        try:
            user = self._db.find_user_by(email=email)
            return bcrypt.checkpw(password.encode(
                    'utf-8'), user.hashed_password)
        except NoResultFound:
            return False
