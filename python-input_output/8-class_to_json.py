#!/usr/bin/python3

"""
This module contains a function that converts a class instance to a JSON serializable dictionary.
"""

def class_to_json(obj):
    """
    Converts a class instance to a JSON serializable dictionary.

    Args:
        obj: The class instance to be converted.

    Returns:
        A dictionary representing the class instance in a JSON serializable format.
    """
    return obj.__dict__
