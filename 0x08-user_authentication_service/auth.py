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

    def destroy_session(self, user_id: int) -> None:
        """ The method updates the corresponding user’s session ID to None """
        if user_id is None:
            return None
        try:
            user = self._db.find_user_by(id=user_id)
            self._db.update_user(user.id, session_id=None)
        except NoResultFound:
            return None

    def get_reset_password_token(self, email: str) -> str:
        """ Implement the Auth.get_reset_password_token method. It take
            an email string argument and returns a string
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            raise ValueError
        token_ = _generate_uuid()
        self._db.update_user(user.id, reset_token=token_)
        return token_

    def update_password(self, reset_token: str, password: str) -> None:
        """ Implement the Auth.update_password method. It takes
            reset_token string argument and a password string argument
            and returns None.
        """
        if reset_token is None or password is None:
            return None
        try:
            user_session = self._db.find_user_by(reset_token=reset_token)
        except NoResultFound:
            raise ValueError
        hashed_password = _hash_password(password)
        self._db.update_user(user_session.id,
                             hashed_password=hashed_password,
                             reset_token=None)
