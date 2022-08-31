n = int(input())
prev1 = prev2 = n
i = -1
d = k = m = 0

while n != 0:
    if n < prev1 and prev1 > prev2:
        if d != 0:
            k = i - d
        if k < m or m == 0:
            m = k
        d = i
    prev1, prev2 = n, prev1
    i += 1
    n = int(input())

print(m)
