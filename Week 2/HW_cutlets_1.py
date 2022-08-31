k, m, n = int(input()),  int(input()),  int(input())

if n <= k:
    print(m * 2)
elif n % k == 0:
    print((n // k) * (m * 2))
elif round(n % k) > (k // 2):
    print((n // k + 1) * (m * 2))
else:
    print(((n // k + 1) * (m * 2)) - m)
