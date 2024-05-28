#!/usr/bin/python3

"""
This script adds command line arguments to a JSON file.
"""

import json
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


try:
    my_list = load_from_json_file("add_item.json")
    my_list.extend(sys.argv[1:])
    save_to_json_file(my_list, "add_item.json")
except Exception:
    my_list = sys.argv[1:]
    save_to_json_file(my_list, "add_item.json")
