#!/usr/bin/env python3
""" Module named 1-async_comprehension """


from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ Using an async comprehensing

    Args: None
    """
    return [number async for number in async_generator()]
