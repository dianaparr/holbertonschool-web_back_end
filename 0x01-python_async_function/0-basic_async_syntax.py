#!/usr/bin/env python3
""" Module named 0-basic_async_syntax """

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ Asynchronous coroutine.

    Args:
        max_delay -> integer (value: 10)

    Return: a float (time random)

    """
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
