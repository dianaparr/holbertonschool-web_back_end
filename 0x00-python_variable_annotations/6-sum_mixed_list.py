#!/usr/bin/env python3
""" Module name 6-sum_mixed_list """

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ Function which takes a list of integers and floats and return
        their sum as a float.

        Args:
            mxd_lst -> List[Union[int, float]]

        Return: sum of mixed list numbers
    """
    return sum(mxd_lst)
