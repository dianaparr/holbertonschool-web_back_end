#!/usr/bin/env python3
""" Module name 9-element_length """

from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Function that return values with the appropriate types"""
    return [(i, len(i)) for i in lst]
