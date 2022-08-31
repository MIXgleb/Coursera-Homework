from itertools import permutations

nk = list(map(int, input().split()))
a = [input().split() for _ in range(nk[1])]
ans = ''

for i in list(map(str, permutations((range(1, nk[0] + 1))))):
    mark = 0
    for j in a:
        if i.find(j[0]) < i.find(j[1])\
                and i.find(j[2]) > i.find(j[3])\
                or i.find(j[0]) > i.find(j[1])\
                and i.find(j[2]) < i.find(j[3]):
            mark += 1
    if mark == nk[1]:
        ans = i
        break
if ans != '':
    [print(ans[3 * (i - 1) + 1], end=' ') for i in range(1, nk[0] + 1)]
else:
    print(0)
