import math


def Squares(n, k):
    global s
    i = 0
    if n != 0:
        while i <= int(math.sqrt(n)):
            i += 1
        # print(i - 1, end=' ')
        s += str(i - 1) + ' '
        Squares(n - (i - 1)**2, k - 1)
    if k == -1:
        n = m
        while i + 1 <= int(math.sqrt(n)):
            i += 1
        # print(i - 1, end=' ')
        n = n - (i - 1)**2
        s = str(i - 1) + ' '
        k = 3
        Squares(n, k)


n = int(input())
m = n
s = ''
Squares(n, 4)
print(s)
