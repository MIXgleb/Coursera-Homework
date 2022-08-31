import math


def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


def perimeter(x1, y1, x2, y2, x3, y3):
    return (distance(x1, y1, x2, y2) +
            distance(x1, y1, x3, y3) +
            distance(x2, y2, x3, y3))


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())

print('{0:.6f}'.format(perimeter(x1, y1, x2, y2, x3, y3)))
