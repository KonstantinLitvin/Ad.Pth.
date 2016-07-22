__author__ = 'KonstantinLitvin'

V = int(input())
T = int(input())

S = V * T

numOfCircles = S//109

print(S - 109 * numOfCircles)
