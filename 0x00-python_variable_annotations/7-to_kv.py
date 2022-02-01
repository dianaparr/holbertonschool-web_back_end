#!/usr/bin/env python3
""" Module name 7-to_kv """

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ Function that takes a string k and an int OR float v as arguments
        and returns a tuple

        Args:
            k -> string
            v -> Union[int, float] -> int | float

        Return: a Tuple, first element is the string and
                second element is the square of the int/float
                (should be annotated as a float).
    """
    return (k, v * v)
