# print('{0:.25f}'.format(0.1))
q = ''


def cubes(n, num):
    global q
    if n == 0:
        return 0
    elif n <= 7:
        q += ('1 ' * n)
    elif int(n**(1 / 3))**3 == n:
        q += str(n) + ' '
    elif int(n**(1 / 3))**3 < n:
        cubes(n - int(n ** (1 / 3)) ** 3, num - 1)
        q += str(int(n ** (1 / 3)) ** 3) + ' '
    if q.count(' ') > 7:
        return 0
    else:
        return q


print(cubes(int(input()), 7))
