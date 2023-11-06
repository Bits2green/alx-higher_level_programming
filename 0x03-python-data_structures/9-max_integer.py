#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return
    largest_integer = my_list[0]
    for i in range(1, len(my_list)):
        if largest_integer < my_list[i]:
            largest_integer = my_list[i]
        else:
            continue
    return largest_integer
