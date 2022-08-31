x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
# if (abs(x2 - x1) == 0 or abs(x2 - x1) == 1 or abs(x2 - x1) == -1) and\
#    (abs(y2 - y1) == 0 or abs(y2 - y1) == 1 or abs(y2 - y1) == -1):
if (x2 - x1) == 0 and (y2 - y1) == 0:
    print('NO')
elif (y2 - y1) in [-1, 0, 1] and (x2 - x1) in [-1, 0, 1]:
    print('YES')
else:
    print('NO')
