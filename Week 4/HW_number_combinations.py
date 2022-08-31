def cnk(n, k):
    if k == 1:
        return n
    if k == n or k == 0:
        return 1
    return cnk(n - 1, k) + cnk(n - 1, k - 1)


print(cnk(int(input()), int(input())))
