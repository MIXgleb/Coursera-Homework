def merge(a, b):
    j = 0
    c = []
    for i in a:
        while j < len(b) and b[j] < i:
            c.append(b[j])
            j += 1
        c.append(i)
    while j < len(b):
        c.append(b[j])
        j += 1
    return c


a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(*merge(a, b))
