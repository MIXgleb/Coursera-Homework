# list = list(map(int, input().split()))
# print(' '.join(map(str, list)))
# print(*list)
list = list(map(int, input().split()))

for i in range(len(list)):
    if list[i] % 2 == 0:
        print(list[i], end=' ')
