#!/usr/bin/env python3
""" Module named 0-simple_helper_function """


from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ The function should return a tuple of size two containing a
        start index and an end index corresponding to the range of
        indexes to return in a list for those particular pagination parameters.

    Args:
        page -> integer
        page_size -> integer

    Return: a tuple of size two containing a start index
            and end index (int, int)
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
