n = int(input())
i = 1
f1 = 1
f2 = 0

while i <= n:
    f = f1 + f2
    f2, f1 = f1, f
    i += 1

print(f2)
