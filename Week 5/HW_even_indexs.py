# list = list(map(int, input().split()))
# print(' '.join(map(str, list)))
# print(*list)
a = list(map(int, input().split()))

for _ in range(len(a)):
    if _ % 2 == 0:
        print(a[_], end=' ')
