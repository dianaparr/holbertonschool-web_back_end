#!/usr/bin/env python3
""" Module named session_auth to the class Auth """


from api.v1.auth.auth import Auth
from typing import Dict
from uuid import UUID, uuid4


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
