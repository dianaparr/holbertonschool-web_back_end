#!/usr/bin/env python3
""" Module named 3-tasks """

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """ Obtain the object asyncio.Task

    Args:
        max_delay -> integer

    Return: asyncio.Task (new task from wait_random)

    """
    return asyncio.create_task(wait_random(max_delay))
