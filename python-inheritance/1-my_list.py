#!/usr/bin/python3

"""
This file contains class MyList that
inherits from list
"""


class MyList(list):
    """
    A custom list class that inherits from the built-in list class.

    This class provides an additional method, print_sorted,
    which prints the elements of the list in sorted order.
    """

    def print_sorted(self):
        """
        Prints the elements of the list in sorted order.

        Returns:
            None
        """
        print(sorted(self))
