#!/usr/bin/env python3
"""
Async routine module
"""
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
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
    delays: List[float] = []
    for _ in range(n):
        delay = await task_wait_random(max_delay)
        if not delays:
            delays.append(delay)
        else:
            for idx, d in enumerate(delays):
                if delay < d:
                    delays.insert(idx, delay)
                    break
                else:
                    delays.append(delay)

    return delays
