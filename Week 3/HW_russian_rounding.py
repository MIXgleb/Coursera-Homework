# print('{0:.25f}'.format(0.1))
# print(float(2**100).as_integer_ratio())

import math

n = float(input())

if n * 10 % 10 < 5:
    print(math.floor(n))
elif n * 10 % 10 >= 5:
    print(math.ceil(n))
