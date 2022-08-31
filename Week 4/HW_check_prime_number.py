import math


def isPrime(n):
    i = 2
    m = n
    while i <= math.sqrt(n):
        if n % i == 0:
            m = i
            return m == n
        else:
            i += 1
    return m == n


n = int(input())

if isPrime(n):
    print('YES')
else:
    print('NO')
