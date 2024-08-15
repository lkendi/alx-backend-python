#!/usr/bin/env python3
"""
Async routine module
"""
from time import perf_counter


wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
    Asynchronous coroutine that measures the total execution time
    for wait_n(n, max_delay) and returns total_time / n

    Args:
        n (int): The number of concurrent tasks to wait for.
        max_delay (int): The maximum delay for each task.

    Returns:
        float: total_time/n
    """
    start_time = perf_counter()
    await wait_n(n, max_delay)
    end_time = perf_counter()
    total_time = end_time - start_time
    return total_time / n
