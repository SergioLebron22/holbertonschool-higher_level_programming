#!/usr/bin/python3

"""
this file contains function inherits_from
"""


def inherits_from(obj, a_class):
    """
    Checks if an object is an instance of
    a subclass (direct or indirect) of a given class.

    Args:
        obj: The object to be checked.
        a_class: The class to be checked against.

    Returns:
        True if the object is an instance of
        a subclass of the given class, False otherwise.
    """
    return issubclass(type(obj), a_class)\
        and type(obj) is not a_class
