#!/usr/bin/env python3
""" Module named 2-measure_runtime """


import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ Run time for four parallel comprehensions

    Args: None

    Return: a float (total runtime)
    """
    end_: float
    start_ = time.perf_counter()

    all_tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*all_tasks)

    end_ = time.perf_counter() - start_
    return end_
