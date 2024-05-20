#!/usr/bin/python3
"""

this file has function add integers

"""


def add_integer(a, b=98):
    """
    This function adds a and b, if b is not passed, default is set to 98
    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(a, float):
        raise TypeError("b must be an integer")
    return int(a + b)
