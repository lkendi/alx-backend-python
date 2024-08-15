#!/usr/bin/env python3
"""
sum_list function module
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Type-annotated function that sums a list of floats

    Args:
        input_list: list of floats

    Returns:
        Sum of the values in the list as a float
    """
    return float(sum(input_list))
