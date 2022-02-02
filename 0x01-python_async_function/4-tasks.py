#!/usr/bin/env python3
""" Module named 1-concurrent_coroutines """

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
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
    # (happens in task 3 module, here just call the function)
    for _ in range(n):
        tasks.append(task_wait_random(max_delay))

    # as_completed() to get tasks as they are completed, in the
    # order of completion.
    for res in asyncio.as_completed(tasks):
        task = await res
        all_delays.append(task)

    return all_delays
