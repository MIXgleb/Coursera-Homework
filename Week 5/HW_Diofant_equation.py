a, b, c, d, e = [int(input()) for _ in range(5)]
i = 0

for x in range(1001):
    if (x - e) != 0 and \
            a * x**3 + b * x**2 + c * x + d == 0:
        i += 1

print(i)
