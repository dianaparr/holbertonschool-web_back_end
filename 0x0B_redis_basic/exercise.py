#!/usr/bin/env python3
""" Module to create Cache class """

import redis
from typing import Optional, Union, Callable
import uuid
import sys


class Cache:
    """ Create a Cache class """
    def __init__(self):
        """ Constructor with:
            - store an instance of the Redis client as a
                private variable named _redis.
            - use the command FLUSHDB to flush the instance.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ The method should:
            - generate a random key
            - store the input data in Redis using the random key
            - return the key
        """
        generate_key = str(uuid.uuid4())
        # redis> SET mykey "Hello"
        self._redis.set(generate_key, data)
        return generate_key

    def get(self, name_key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """ A get method that take a key string argument and
            an optional Callable argument named fn
        """
        value = self._redis.get(name_key)
        if fn:
            return fn(value)
        return value

    def get_str(self, name_key: str) -> str:
        """ That will automatically parametrize Cache.get
            with the correct conversion function.
        """
        value = self._redis.get(name_key)
        return value.decode('utf-8')

    def get_int(self, name_key: str) -> int:
        """ That will automatically parametrize Cache.get
            with the correct conversion function.
        """
        # To request the native byte order of the host system,
        # use sys.byteorder as the byte order value
        return int.from_bytes(name_key, sys.byteorder)
