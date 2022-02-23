#!/usr/bin/env python3
""" Class DB """

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError

from user import Base
from user import User


class DB:
    """ DB Class """

    def __init__(self) -> None:
        """ Initialize a new DB instance """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """ Memoized session object """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """ The method should save the user to the database.
        """
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, **kwargs) -> User:
        """ This method takes in arbitrary keyword arguments and returns
            the first row found in the users table as filtered by the method’s
            input arguments.
        """
        if kwargs is None:
            raise InvalidRequestError
        user = self._session.query(User).filter_by(**kwargs).first()
        if user is None:
            raise NoResultFound
        return user

    def update_user(self, user_id: int, **kwargs) -> None:
        """ Implement the DB.update_user method that takes as argument
            a required user_id integer and arbitrary keyword arguments,
            and returns None
        """
        user_updt = self.find_user_by(id=user_id)
        for k, v in kwargs.items():
            if hasattr(user_updt, k):
                setattr(user_updt, k, v)
            else:
                raise ValueError
        self._session.commit()
