#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list and len(my_list):
        y = 0
        x = 0
        for tup in my_list:
            y += (tup[0] * tup[1])
            x += tup[1]
        return (y / x)
    return 0