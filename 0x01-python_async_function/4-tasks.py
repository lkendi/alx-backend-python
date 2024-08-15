#!/usr/bin/env python3
"""
Async routine module
"""
from typing import List
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous coroutine that spawns task_wait_random n times with
    the specified max_delay and returns a list of the delays in ascending order
    without using sort because of concurrency.

    Args:
        n (int): The number of random delays to wait for.
        max_delay (int): The maximum delay for each wait.

    Returns:
        List[float]: A list of delays in ascending order.
    """
    tasks = [(task_wait_random(max_delay)) for _ in range(n)]
    delays = []

    for task in asyncio.as_completed((tasks)):
        delay = await task
        delays.append(delay)

    return delays
