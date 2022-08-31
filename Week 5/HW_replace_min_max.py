a = list(map(int, input().split()))

for i in range(len(a)):
    if a[i] == max(a):
        maxind = i
    if a[i] == min(a):
        minind = i

a[maxind], a[minind] = a[minind], a[maxind]

print(*a)
