# print('{0:.25f}'.format(0.1))
# print(float(2**100).as_integer_ratio())

import math

x = int(input())
s2 = 0
s1 = 0
n = 0

while x != 0:
    s1 += x
    s2 += x**2
    n += 1
    x = int(input())

print(math.sqrt((s2 - s1**2 / n) / (n - 1)))
