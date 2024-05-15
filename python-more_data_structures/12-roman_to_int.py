#!/usr/bin/python3

def roman_to_int(roman_string):
    if roman_string is None or \
            isinstance(roman_string, str) is False:
        return 0

    result = 0
    roman_num = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    for i in range(len(roman_string)):

        current = roman_num[roman_string[i]]
        prev = roman_num[roman_string[i - 1]]

        if i > 0 and prev < current:
            result += current - 2 * prev
        else:
            result += current

    return result
