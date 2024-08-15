#!/usr/bin/env python3
"""
Async routine module
"""
from time import time
import asyncio


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Asynchronous coroutine that measures the total execution time
    for wait_n(n, max_delay) and returns total_time / n

    Args:
        n (int): The number of concurrent tasks to wait for.
        max_delay (int): The maximum delay for each task.

    Returns:
        float: total_time/n
    """
    start_time = time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time()
    total_time = end_time - start_time
    return (total_time / n)
