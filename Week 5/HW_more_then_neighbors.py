# list = list(map(int, input().split()))
# print(' '.join(map(str, list)))
# print(*list)
list = list(map(int, input().split()))
j = 0

for i in range(1, len(list) - 1):
    if list[i] > list[i - 1] and list[i] > list[i + 1]:
        j += 1

print(j)
