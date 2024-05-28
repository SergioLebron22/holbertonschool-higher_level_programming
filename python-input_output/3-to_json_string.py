#!/usr/bin/python3

"""
This module provides a function to convert a Python object to a JSON-formatted string.
"""


import json

def to_json_string(my_obj):
    """
    Converts a Python object to a JSON-formatted string.

    Args:
        my_obj: The Python object to be converted.

    Returns:
        A JSON-formatted string representing the Python object.
    """
    return json.dumps(my_obj)
