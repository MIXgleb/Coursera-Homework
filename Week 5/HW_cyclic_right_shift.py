a = list(map(int, input().split()))
b = a[-1]

for i in range(len(a) - 1):
    a[-1 - i] = a[-2 - i]

a[0] = b

print(*a)
