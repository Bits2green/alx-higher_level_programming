#!/usr/bin/python3

for num in range(0, 8):
    for a in range(num + 1, 10):
        print("{:d}{:d}".format(num, a), end=', ')
print("{:d}{:d}".format(num + 1, a))
