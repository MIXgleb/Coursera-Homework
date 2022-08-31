a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a == 0:
    if b == 0:
        print('INF')
    else:
        print('NO')
elif c * (-b / a) + d != 0 and b % a == 0:
    print(-b // a)
else:
    print('NO')
