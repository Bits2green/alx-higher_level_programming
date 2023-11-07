#!/usr/bin/python3
from sys import argv
sum = 0
for j in argv[1:]:
    sum += int(j)
print("{:d}".format(sum))
