def intersection(a, b):
    j = 0
    c = []
    for i in a:
        while j < len(b) and b[j] <= i:
            if b[j] == i:
                c.append(i)
                j += 1
            elif b[j] < i:
                j += 1
    return c


a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(*intersection(a, b))
