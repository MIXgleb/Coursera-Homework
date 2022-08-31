n = -1
d = 0
i = 0

while n != 0:
    d = n
    n = int(input())
    if n <= d:
        continue
    i += 1

print(i - 1)
