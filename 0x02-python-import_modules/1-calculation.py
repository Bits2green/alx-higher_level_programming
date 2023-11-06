#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

a = 10
b = 5

sums = add(a, b)
diff = abs(sub(a, b))
prod = mul(a, b)
quo = div(a, b)

print(f"sum = {sums}, difference = {diff}, product = {prod}, quotient = {quo}")

