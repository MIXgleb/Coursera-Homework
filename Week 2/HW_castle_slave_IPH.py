a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
if a > 0 and b > 0 and c > 0 and d > 0 and e > 0:
    if a <= d:
        if b <= e or c <= e:
            print('YES')
        else:
            print('NO')
    elif b <= d:
        if a <= e or c <= e:
            print('YES')
        else:
            print('NO')
    elif c <= d:
        if a <= e or b <= e:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')
else:
    print('NO')
