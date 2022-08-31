a, b, c, d, e, f = (float(input()) for _ in range(6))

det = a * d - b * c
detX = e * d - b * f
detY = a * f - e * c

if a == b == c == d == e == f == 0:
    print(5)
elif b == d == 0 and (e * c == f * a or a == 0 or c == 0):
    print(3, end=' ')
    print(e / a if c == 0 else f / c)
elif a == c == 0 and (e * d == f * b or b == 0 or d == 0):
    print(4, end=' ')
    print(e / b if d == 0 else f / d)
elif det == 0:
    print(0)
elif b != 0 and d != 0 and a / b == c / d and e / b == f / d:
    print(1, - a / b, e / b)
else:
    print(2, detX / det, detY / det)
