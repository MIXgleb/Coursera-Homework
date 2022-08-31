mySet = set()

for i in list(map(int, input().split())):
    if i in mySet:
        print('YES')
    else:
        print('NO')
    mySet.add(i)
