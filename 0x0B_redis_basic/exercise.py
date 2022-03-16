#!/usr/bin/env python3
""" Module to create Cache class """

import redis
from typing import Union
import uuid

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
