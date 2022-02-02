#!/usr/bin/env python3
""" Module named 1-concurrent_coroutines """

import asyncio
import random
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ An asynchronous routine that run multiple
        coroutines at the same time with async.

    Args:
        n -> int
        max_delay -> integer

    Return: list of all delays (float values)

    """
    all_delays = list()
    tasks = list()

    # create_task() to schedule the execution of a coroutine object.
    for _ in range(n):
        tasks.append(asyncio.create_task(wait_random(max_delay)))

    # as_completed() to get tasks as they are completed, in the
    # order of completion.
    for res in asyncio.as_completed(tasks):
        all_delays.append(await res)

    return all_delays
