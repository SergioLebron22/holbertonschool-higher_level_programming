#!/usr/bin/python3


import csv
import json


def convert_csv_to_json(filename):

    data = []

    try:
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)

            data = [rows for rows in reader]

    except FileNotFoundError:
        return False

    try:
        with open("data.json", 'w') as jFile:
            json.dump(data, jFile, indent=4)

    except FileNotFoundError:
        return False

    return True
