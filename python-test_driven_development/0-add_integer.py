#!/usr/bin/python3

def add_integer(a, b=98):
    """
    Adds two integers and returns the sum.

    Args:
        a (int): The first integer.
        b (int, optional): The second integer. Defaults to 98.

    Returns:
        int: The sum of the two integers.

    Raises:
        TypeError: If either `a` or `b` is not an integer.

    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(a, float):
        raise TypeError("b must be an integer")
    return int(a + b)
