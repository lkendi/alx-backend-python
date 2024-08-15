#!/usr/bin/env python3
"""
Asynchronous coroutine module
"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay between 0 and
        max_delay (included and float value) seconds and eventually returns it

    Args:
        max_delay (int) : max number of seconds that the delay can be

    Returns:
        The delay value
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
