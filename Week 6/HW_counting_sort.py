def countSort(a):
    new = [0] * 101
    for i in a:
        new[i] += 1
    for j in range(len(new)):
        print((str(j) + ' ') * new[j], end='')


countSort(list(map(int, input().split())))
