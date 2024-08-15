#!/usr/bin/env python3
"""
sum_mixed_list function module
"""
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """
    Type-annotated function that sums a list of integers and floats

    Args:
        mxd_list - list of integers and floats

    Returns:
        sum of the integers and floats in the list as a float
    """
    return float(sum(mxd_list))
