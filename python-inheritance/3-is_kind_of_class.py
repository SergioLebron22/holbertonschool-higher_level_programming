#!/usr/bin/python3
"""
this file contains function is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance of a
    given class or a subclass of it.

    Args:
        obj: The object to be checked.
        a_class: The class to check against.

    Returns:
        True if the object is an
        instance of the class or a subclass of it,
        False otherwise.
    """
    return isinstance(obj, a_class)
