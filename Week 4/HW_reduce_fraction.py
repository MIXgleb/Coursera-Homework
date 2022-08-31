def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def ReduceFraction(n, m):
    return n // gcd(n, m), m // gcd(n, m)


print(*ReduceFraction(int(input()), int(input())))
