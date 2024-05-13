#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    new_list = my_list.copy()

    if idx < 0:
        return new_list
    elif idx > len(new_list) - 1:
        return new_list

    for i in range(len(new_list)):
        if i == idx:
            new_list[i] = element
            return new_list
