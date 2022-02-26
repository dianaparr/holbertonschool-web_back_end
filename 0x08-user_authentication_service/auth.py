#!/usr/bin/env python3
""" Module called auth """


import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
from uuid import uuid4
from typing import Union


def _hash_password(password: str) -> str:
    """ Method that takes in a password string arguments and returns bytes. """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def _generate_uuid() -> str:
    """ Method that return a string representation of a new uuid """
    return str(uuid4())


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

    def create_session(self, email: str) -> str:
        """ The method should find the user corresponding to the email,
            generate a new UUID and store it in the database as the user’s
            session_id, then return the session ID.
        """
        try:
            user = self._db.find_user_by(email=email)
            sessionID = _generate_uuid()
            self._db.update_user(user.id, session_id=sessionID)
            return sessionID
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> Union[str, None]:
        """ Method to find user by session ID.

        Return:
                User or None if the session ID is None or not user is found.
        """
        if session_id is None:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return None
