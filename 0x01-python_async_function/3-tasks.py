#!/usr/bin/env python3
"""
Module
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Regular function that takes an int and returns a asyncio.Task

    Args:
        max_delay (int): The maximum delay for the task.

    Returns:
        asyncio.Task: The created task.
    """
    return asyncio.create_task(wait_random(max_delay))
