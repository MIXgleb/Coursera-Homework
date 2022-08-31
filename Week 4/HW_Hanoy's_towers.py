def tower(n, st, fin):
    if n == 1:
        print(n, st, fin)
    else:
        tmp = 6 - st - fin
        tower(n - 1, st, tmp)
        print(n, st, fin)
        tower(n - 1, tmp, fin)


tower(int(input()), 1, 3)
