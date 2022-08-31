a = list(map(int, input().split()))
i = 0

while i <= len(a) - 1:
    if a[i] != 0:
        print(a[i], end=' ')
    i += 1

print(*list('0' * a.count(0)))
