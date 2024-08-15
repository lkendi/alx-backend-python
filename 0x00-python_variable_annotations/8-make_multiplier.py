#!/usr/bin/env python3
"""
make_multiplier function module
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Type-annotated function that returns a multiplier function.

    Args:
        multiplier (float): The multiplier value.

    Returns:
        Callable: Function that returns the product of a float input
                    and the multiplier.
    """
    def multiply(number: float) -> float:
        return number * multiplier

    return multiply
