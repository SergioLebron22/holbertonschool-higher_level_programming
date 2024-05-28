#!/usr/bin/python3

"""
This file contains the fucntion save_to_json_file
"""


import json


def save_to_json_file(my_obj, filename):
    """
    Save the given object to a JSON file.

    Args:
        my_obj: The object to be saved.
        filename: The name of the file to save the object to.

    Returns:
        The number of characters written to the file.

    Raises:
        IOError: If there is an error writing to the file.
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(json.dumps(my_obj))
