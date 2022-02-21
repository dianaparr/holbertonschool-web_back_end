#!/usr/bin/env python3
""" Module named session_db_auth to the class SessionExpAuth """


from api.v1.auth.session_exp_auth import SessionExpAuth
from models.user_session import UserSession
from os import getenv
from datetime import datetime, timedelta


class SessionDBAuth(SessionExpAuth):
    """ Class to new authentication system, based on Session ID
        stored in database
    """
    def create_session(self, user_id=None):
        """ Creates and stores new instance of UserSession and returns
            the Session ID.
        """
        try:
            new_session_id = super().create_session(user_id)
        except Exception:
            return None

        new_session = UserSession()
        new_session.user_id = user_id
        new_session.session_id = new_session_id
        new_session.save()

        return new_session_id

    def user_id_for_session_id(self, session_id=None):
        """ Returns the User ID by requesting UserSession in
            the database based on session_id
        """
        if session_id is None:
            return None

        UserSession.load_from_file()
        usr_session = UserSession.search({'session_id': session_id})
        if not usr_session:
            return None
        this_user = usr_session[0]
        if this_user is None:
            return None
        duration_session = this_user.created_at + \
            timedelta(seconds=self.session_duration)
        if duration_session < datetime.now():
            return None

        return this_user.user_id

    def destroy_session(self, request=None):
        """ Destroys the UserSession based on the Session ID
            from the request cookie
        """
        if request is None or self.session_cookie(request) is None:
            return False

        sessions = UserSession.all()
        for session in sessions:
            if session.session_id == self.session_cookie(request):
                del session

        return True
