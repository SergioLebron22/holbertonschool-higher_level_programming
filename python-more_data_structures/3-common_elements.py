#!/usr/bin/python3

def common_elements(set_1, set_2):
    new_set = set()

    for val in set_1:
        for val2 in set_2:
            if val == val2:
                new_set.add(val)

    return new_set
