#!/usr/bin/env python3

from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):

    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        if self.__radius >= 0:
            return pi * self.__radius ** 2

    def perimeter(self):
        if self.__radius >= 0:
            return 2 * pi * self.__radius


class Rectangle(Shape):

    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        return (2 * self.__width) + (2 * self.__height)


def shape_info(obj):
    print(f"Area: {obj.area()}")
    print(f"Perimeter: {obj.perimeter()}")
