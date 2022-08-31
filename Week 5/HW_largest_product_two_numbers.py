a = list(map(int, input().split()))

min1 = min(a)
max1 = max(a)
a.remove(min1)
a.remove(max1)
min2 = min(a)
max2 = max(a)

if max2 * max1 > min2 * min1:
    print(max2, max1)
else:
    print(min1, min2)
