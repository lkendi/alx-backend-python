#!/usr/bin/env python3
"""
Duck-typing module
"""
from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Returns the first element of a list if the list is not empty.

    Args:
        lst (list): The input list.

    Returns:
        The first element of the list, or None if the list is empty.
    """

    if lst:
        return lst[0]
    else:
        return None
