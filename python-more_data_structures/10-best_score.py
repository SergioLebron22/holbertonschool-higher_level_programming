#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None or not isinstance(a_dictionary, dict):
        return None

    if len(a_dictionary) == 0:
        return None

    high_val = 0
    best_key = None

    for k, v in a_dictionary.items():
        if v > high_val:
            high_val = v
            best_key = k

    return best_key
