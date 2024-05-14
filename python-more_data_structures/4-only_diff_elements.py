#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    new_set = set()

    for val in set_1:
        if val not in set_2:
            new_set.add(val)

    for val2 in set_2:
        if val2 not in set_1:
            new_set.add(val2)

    return new_set
