#!/usr/bin/python3

"""
this file contains the function lookup
"""


def lookup(obj):
    """
    Returns a list of all attributes
    and methods of the given object.

    Args:
        obj: The object to inspect.

    Returns:
        A list of strings representing the
        attributes and methods of the object.
    """
    return dir(obj)
