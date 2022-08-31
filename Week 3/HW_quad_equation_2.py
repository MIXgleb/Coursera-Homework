# print('{0:.25f}'.format(0.1))
# print(float(2**100).as_integer_ratio())

import math

a = float(input())
b = float(input())
c = float(input())

d = b**2 - 4 * a * c

if a == 0 and b == 0 and c == 0:
    print(3)
elif a == 0 and b != 0:
    print(1, '{0:.6f}'.format(- c / b))
elif (a != 0 and d < 0) or (a == 0 and b == 0 and c != 0):
    print(0)
elif a != 0 and d == 0:
    print(1, '{0:.6f}'.format(- b / (2 * a)))
elif a != 0 and d > 0:
    print(2, min('{0:.6f}'.format((- b - math.sqrt(d)) / (2 * a)),
                 '{0:.6f}'.format((- b + math.sqrt(d)) / (2 * a))),
          max('{0:.6f}'.format((- b - math.sqrt(d)) / (2 * a)),
              '{0:.6f}'.format((- b + math.sqrt(d)) / (2 * a))))
