#!/usr/bin/python3

def uppercase(str):
    for character in str:
        if ord(character) >= 97 and ord(character) <= 122:
            character = chr(ord(character) - 32)
        print("{:s}".format(character), end='')

    print('\n', end="")
