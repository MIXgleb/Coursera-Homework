def cubes(n, num):
    if num == 0:
        return 0
    q = int(n ** (1 / 3))
    if q ** 3 == n:
        return str(q ** 3)
    while q > 0:
        if cubes(n - q ** 3, num - 1) != 0:
            return str(q ** 3) + " " + cubes(n - q ** 3, num - 1)
        q -= 1
    return 0


print(cubes(int(input()), 7))
