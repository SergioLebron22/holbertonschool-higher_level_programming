#!/usr/bin/python3

"""
This file contains append_write function
"""


def append_write(filename="", text=""):
    """
    Appends text to a file.

    Args:
        filename (str): The name of the file to append to.
        text (str): The text to append to the file.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
