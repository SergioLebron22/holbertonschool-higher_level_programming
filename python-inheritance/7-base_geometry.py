#!/usr/bin/python3

"""
This file contains class BaseGeometry
"""


class BaseGeometry:
    """
    This is the base class for geometry objects.

    Methods:
    - area(): Raises an exception indicating 
    that the method is not implemented.
    - integer_validator(name, value): Validates 
    if the given value is an integer and greater than 0.
    """

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if isinstance(value, bool):
            raise TypeError(f"{name} must be an integer")
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
