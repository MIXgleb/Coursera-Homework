a = list(map(int, input().split()))
kc = list(map(int, input().split()))
a.append(a[-1])

for i in range(len(a) - 1, kc[0], -1):
    a[i] = a[i - 1]

a[kc[0]] = kc[1]

print(*a)
