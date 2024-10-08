#!/usr/bin/env python3
"""
Async routine module
"""
from typing import List
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous coroutine that spawns wait_random n times with
    the specified max_delay and returns a list of the delays in ascending order
    without using sort because of concurrency.

    Args:
        n (int): The number of random delays to wait for.
        max_delay (int): The maximum delay for each wait.

    Returns:
        List[float]: A list of delays in ascending order.
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays = []
    while tasks:
        done, pending = await asyncio.wait(
                tasks, return_when=asyncio.FIRST_COMPLETED)
        for task in done:
            delays.append(task.result())
        tasks = pending

    return delays
