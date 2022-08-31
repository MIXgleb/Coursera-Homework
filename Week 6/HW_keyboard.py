n = int(input())
listN = list(map(int, input().split()))
k = int(input())
listK = list(map(int, input().split()))

for i in listK:
    listN[i - 1] -= 1

for j in range(n):
    if listN[j] < 0:
        print('YES')
    else:
        print('NO')
