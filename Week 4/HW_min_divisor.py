import math


def minDivisor(n):
    i = 2
    while i <= math.sqrt(n):
        if n % i == 0:
            return i
        else:
            i += 1
    return n


n = int(input())

print(minDivisor(n))
