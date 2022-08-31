a, k = list(input().split()), int(input())

for i in range(k, len(a) - 1):
    a[i] = a[i + 1]

a.pop()

print(*a)
