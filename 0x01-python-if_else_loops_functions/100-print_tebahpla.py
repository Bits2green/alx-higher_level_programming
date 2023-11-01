#!/usr/bin/python3

for num in range(26):
    if num % 2 == 0:
        print('{:c}'.format(122 - num), end='')
    else:
        print('{:c}'.format(90 - num), end='')
