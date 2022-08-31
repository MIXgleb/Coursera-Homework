a = list(map(int, input().split()))

if len(a) == 3:
    print(*a)
else:
    min1 = min(a)
    max1 = max(a)
    a.remove(min1)
    a.remove(max1)
    min2 = min(a)
    max2 = max(a)
    a.remove(max2)
    max3 = max(a)

    if max2 * max1 * max3 > min2 * min1 * max1:
        print(max1, max2, max3)
    else:
        print(max1, min1, min2)
