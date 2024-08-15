#!/usr/bin/env python3
"""
to_kv function module
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple containing a string key and the square of a number.

    Args:
        k (str): string value returned in the tuple.
        v (Union[int, float]): number to be squared (either int or float)

    Returns:
        Tuple[str, float]: A tuple containing the string and squared value.
    """
    return (k, (v * v))
