mySet = set(range(1, int(input()) + 1))
data = input()

while str(data) != 'HELP':
    data = set(map(int, data.split()))
    if 2 * len(mySet & data) <= len(mySet):
        print('NO')
        mySet -= data
    else:
        print('YES')
        mySet &= data
    data = input()

print(*sorted(mySet))
