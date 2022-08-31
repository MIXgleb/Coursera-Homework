def fourSquare(n, num):
    if num == 0:
        return 0
    q = int(n**(1 / 2))
    if q**2 == n:
        return str(q)
    while q > 0:
        if fourSquare(n - q**2, num - 1) != 0:
            return str(q) + " " + fourSquare(n - q**2, num - 1)
        q -= 1
    return 0


n = int(input())
print(fourSquare(n, 4))
