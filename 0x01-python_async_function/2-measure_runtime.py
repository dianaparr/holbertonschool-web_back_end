#!/usr/bin/env python3
""" Module named 2-measure_runtime """

import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ To measure an approximate elapsed time

    Args:
        n -> int
        max_delay -> integer

    Return: total_time / n (float value)

    """
    total_elapsed_time: float
    start_ = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end_ = time.perf_counter() - start_
    total_elapsed_time = end_ / n

    return total_elapsed_time
