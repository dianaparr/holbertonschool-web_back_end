#!/usr/bin/env python3
""" Module name 2-floor """


def floor(n: float) -> int:
    """ Function which takes a float n as argument and returns
    the floor of the float.

        Args:
            n -> float

        Return: a integer (the floor of the float)
    """
    if (n >= 0):
        return int(n)
    else:
        return int(n) - 1
