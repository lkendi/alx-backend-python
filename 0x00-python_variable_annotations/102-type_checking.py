#!/usr/bin/env python3
"""
Mypy type-checking module
"""
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Returns a zoomed version of the input list by
    repeating each element a specified number of times.

    Args:
        lst (Tuple): The input list to be zoomed.
        factor (int): The number of times to
                repeat each element. Defaults to 2.

    Returns:
        List: The zoomed list.
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
