__author__ = 'KonstantinLitvin'

import math

H = int(input())
A = int(input())
B = int(input())

x = math.ceil((H - B) / (A - B))

print(x)

