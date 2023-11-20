#!/usr/bin/python3

def magic_calculation(a, b):
    res = 0

    for x in range(1, 3):
        try:
            if x > a:
                raise Exception('Too far')

            results += a ** b / x
        except:
            results = b + a
            break

    return results
