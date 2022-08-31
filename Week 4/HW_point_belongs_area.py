def isPointInArea(x, y):
    return ((x + 1)**2 + (y - 1)**2 <= 4 and
            x + y >= 0 and y - 2 * x >= 2) or \
           ((x + 1)**2 + (y - 1)**2 >= 4 and
            x + y <= 0 and y - 2 * x <= 2)


x = float(input())
y = float(input())

if isPointInArea(x, y):
    print('YES')
else:
    print('NO')
