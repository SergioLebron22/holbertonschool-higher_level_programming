def multiply_list_map(my_list=[], number=0):
    result = map(lambda a : a * number, my_list)
    return list(result)
