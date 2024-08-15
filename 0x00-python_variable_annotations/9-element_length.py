#!/usr/bin/env python3
"""
Variable annotations module
"""
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples containing each value
    in the input list along with its length.

    Args:
        lst (Iterable[Sequence]): list of sequences.

    Returns:
        List[Tuple[Sequence, int]]: List of tuples, each containing a sequence
                in the list and its corresponding length
    """
    return [(i, len(i)) for i in lst]
