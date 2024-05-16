#!/usr/bin/python3
"""
this file contains the Square class
"""


class Square:
    """
    A class representing a square.

    Attributes:
        __size: size of the square

    Methods:
        None
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
