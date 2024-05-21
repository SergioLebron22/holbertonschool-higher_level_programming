#!/usr/bin/python3

"""
this file contains the function say_my_name
"""


def say_my_name(first_name, last_name=""):
    """
    Prints the name by concatenating the first name and last name.

    Args:
        first_name (str): The first name.
        last_name (str, optional): The last name. Defaults to "".

    Raises:
        TypeError: If either `first_name` or `last_name` is not a string.

    Returns:
        None
    """
    if not isinstance(first_name, str): 
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    
    print(f"My name is {first_name} {last_name}")
