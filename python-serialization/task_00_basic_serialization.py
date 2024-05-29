#!/usr/bin/python3


import json


def serialize_and_save_to_file(data, filename):
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(json.dumps(data))


def load_and_deserialize(filename):
    with open(filename, encoding="utf-8") as f:
        return json.loads(f.read())
