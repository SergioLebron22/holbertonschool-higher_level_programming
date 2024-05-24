#!/usr/bin/env python3

"""
This module defines an abstract base class (ABC)
called Animal and two concrete classes,
Dog and Cat, that inherit from Animal.
"""


from abc import ABC, abstractmethod


class Animal(ABC):
    """
    An abstract base class representing an animal.
    """

    @abstractmethod
    def sound(self):
        """
        Abstract method that should be implemented by
        subclasses to make a sound.
        """
        pass


class Dog(Animal):
    """
    A class representing a dog, which is a type of animal.
    """

    def sound(self):
        """
        Makes a barking sound.
        """
        return "Bark"


class Cat(Animal):
    """
    A class representing a cat, which is a type of animal.
    """

    def sound(self):
        """
        Makes a meowing sound.
        """
        return "Meow"
