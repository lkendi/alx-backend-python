#!/usr/bin/env python3
"""
Measure runtime module
"""
from time import time
import asyncio


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Async coroutine  that will execute async_comprehension
    four times in parallel using asyncio.gather, measure
    the total runtime and return it.

    Returns:
        float: The total runtime
    """
    start = time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end = time()
    return end - start
