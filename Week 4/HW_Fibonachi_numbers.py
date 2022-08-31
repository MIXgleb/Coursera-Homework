def phib(n):
    if n <= 0:
        return 1
    return phib(n - 2) + phib(n - 1)


print(phib(int(input()) - 2))
