#!/usr/bin/python3
"""
this file contains the Square class
"""


class Square:
    """
    Represents a square.

    Attributes:
        __size (int): The size of the square.

    Methods:
        __init__(self, size=0): Initializes a Square object.
        area(self): Calculates the area of the square.
    """

    def __init__(self, size=0, position=(0, 0)):
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
        if not isinstance(position, tuple) or len(position) != 2\
        or not isinstance(position[0], int) or not isinstance(position[1], int)\
        or position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = size
        self.__position = position

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

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):

        if self.__size == 0:
            print()
        else:
            i = 0
            while i is not self.__position[1]:
                print()
                i += 1
            for i in range(self.__size):
                pos = 0
                while pos is not self.__position[0]:
                    print(" ",end='')
                    pos += 1
                for j in range(self.__size):
                    print("#", end="")
                print()

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2\
        or not isinstance(value[0], int) or not isinstance(value[1], int)\
        or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

