n = int(input())
k = 0
i = 1
d = 0

while n != 0:
    if n == k:
        i += 1
    else:
        i = 1
    if i > d:
        d = i
    k = n
    n = int(input())

print(d)
