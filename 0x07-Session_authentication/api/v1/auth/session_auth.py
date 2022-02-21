#!/usr/bin/env python3
""" Module named session_auth to the class Auth """


from api.v1.auth.auth import Auth
from typing import Dict, TypeVar
from uuid import UUID, uuid4
from models.user import User


class SessionAuth(Auth):
    """ Class SessionAuth for creating a new
        authentication mechanism
    """
    user_id_by_session_id: Dict = {}

    def create_session(self, user_id: str = None) -> str:
        """ Instance method that creates a
            session ID for a user_id.
        """
        if user_id is None or type(user_id) is not str:
            return None

        new_session_id: str = str(uuid4())
        self.user_id_by_session_id[new_session_id] = user_id

        # the same user_id can have multiple Session ID - indeed,
        # the user_id is the value in the dictionary
        # user_id_by_session_id
        return new_session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ Instance method that returns a User ID
            based on a Session ID.

            Return: the User ID
        """
        if (session_id is None or type(session_id) is not str):
            return None

        # for accessing in a dictionary a value based on key.
        user_ID: str = self.user_id_by_session_id.get(session_id)

        return user_ID

    def current_user(self, request=None):
        """ Instance method that returns a User instance based on
            a cookie value.

            Return: get a User based on his session ID.
        """
        new_session_id: str = self.session_cookie(request)
        if new_session_id is None:
            return None
        user_ID: str = self.user_id_for_session_id(new_session_id)
        get_user: TypeVar('User') = User.get(user_ID)

        return get_user

    def destroy_session(self, request=None):
        """ Instance method that deletes the user session/logout """
        if request is None:
            return False
        new_session_id = self.session_cookie(request)
        if not new_session_id:
            return False
        user_ID = self.user_id_for_session_id(new_session_id)
        if not user_ID:
            return False
        del self.user_id_by_session_id[new_session_id]
        return True
