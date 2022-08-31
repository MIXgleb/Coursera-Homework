n = int(input())
k = n
m = n
i = 1
j = 1
d = 0
c = 0

while n != 0:
    if n > k:
        i += 1
    else:
        i = 1
    if i > d:
        d = i

    if n < m:
        j += 1
    else:
        j = 1
    if j > c:
        c = j

    m = n
    k = n
    n = int(input())

print(max(c, d))
