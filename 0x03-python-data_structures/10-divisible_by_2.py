#!/usr/bin/python3

def divisible_by_2(my_list=[10, 4,3,3,7,65,43]):
    for i in my_list:
        if i % 2 == 0:
            print("{:d} is divisible by {:d}".format(i, 2))
        else:
            print("{:d} is not divisible by {:d}".format(i, 2))
