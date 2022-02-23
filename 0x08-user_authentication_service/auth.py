#!/usr/bin/env python3
""" Module called auth """


import bcrypt


def _hash_password(password: str) -> str:
    """ Method that takes in a password string arguments and returns bytes. """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
