#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    length_of_a = len(tuple_a)
    length_of_b = len(tuple_b)
    if length_of_a < 1:
        tuple_a = (0, 0)
    elif length_of_a < 2:
        tuple_a = (tuple_a[0], 0)
    if length_of_b < 1:
        tuple_b = (0, 0)
    elif length_of_b < 2:
        tuple_b = (tuple_b[0], 0)

    result = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return result
