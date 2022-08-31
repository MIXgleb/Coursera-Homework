def justSquares(i):
    n = int(input())
    if n != 0:
        if int(n**(1 / 2))**2 == n:
            i += 1
            justSquares(i)
            print(n)
        else:
            justSquares(i)
    elif i == 0:
        print(0)


justSquares(0)
