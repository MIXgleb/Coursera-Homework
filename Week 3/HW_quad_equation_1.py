# print('{0:.25f}'.format(0.1))
# print(float(2**100).as_integer_ratio())

import math

a = float(input())
b = float(input())
c = float(input())

d = b**2 - 4 * a * c

if d == 0:
    print('{0:.6f}'.format(- b / (2 * a)))
elif d > 0:
    print(min('{0:.6f}'.format((- b - math.sqrt(d)) / (2 * a)),
              '{0:.6f}'.format((- b + math.sqrt(d)) / (2 * a))),
          max('{0:.6f}'.format((- b - math.sqrt(d)) / (2 * a)),
              '{0:.6f}'.format((- b + math.sqrt(d)) / (2 * a))))
elif d < 0:
    print('')
