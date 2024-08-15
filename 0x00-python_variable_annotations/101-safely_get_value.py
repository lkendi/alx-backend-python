#!/usr/bin/env python3
"""
Module
"""
from typing import Union, Any, Mapping, TypeVar


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    Retrieves the value associated with the given key from the dictionary.

    Args:
        dct (Mapping): The dictionary to retrieve the value from.
        key (Any): The key to retrieve the value for.
        default (Union[T, None], optional): The default value to return if the key is not found. Defaults to None.

    Returns:
        Union[Any, T]: The value associated with the given key or the default value if the key is not found.
    """
    if key in dct:
        return dct[key]
    else:
        return default
