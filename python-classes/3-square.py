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
        area: calculates the area of the square
    """
    class Square:
        def __init__(self, size=0):
            """
            Initializes a Square object.

            Args:
                size (int): The size of the square. Defaults to 0.

            Raises:
                TypeError: If size is not an integer.
                ValueError: If size is less than 0.
            """
            if not isinstance(size, int):
                raise TypeError("size must be an integer")
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size

        def area(self):
            """
            Calculates the area of the square.

            Returns:
                int: The area of the square.
            """
            return self.__size ** 2
