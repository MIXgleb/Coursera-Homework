# print('{0:.25f}'.format(0.1))
from math import sqrt


def onlysquares():
    n = int(input())
    while n != 0:
        if int(sqrt(n))**2 == n:
            return str(onlysquares()) + str(n) + ' '
        return onlysquares()
    return ''


x = str(onlysquares())
print(0) if len(x) == 0 else print(x)
