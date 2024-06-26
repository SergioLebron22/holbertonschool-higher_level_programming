#!/usr/bin/python3
"""
This file Contains function is_same_class
"""


def is_same_class(obj, a_class):
    """
    Checks if an object is an instance of a given class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if the object is an instance of the class, False otherwise.
    """
    return type(obj) is a_class
