n = int(input())
i = 0
f1 = 1
f2 = 0
f = 0

while f <= n:
    f = f1 + f2
    f2, f1 = f1, f
    i += 1

if f2 != n:
    i = -1

print(i)
