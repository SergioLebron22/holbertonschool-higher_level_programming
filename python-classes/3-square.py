#!/usr/bin/python3
"""
this file contains the Square class
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
        if not isinstance(self.__size, int):
            raise TypeError
        if self.__size < 0:
            raise ValueError

        return self.__size ** 2
