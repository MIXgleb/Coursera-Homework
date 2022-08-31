# list = list(map(int, input().split()))
# print(' '.join(map(str, list)))
# print(*list)
list = list(map(int, input().split()))
max = list[0]
j = 0

for i in range(len(list)):
    if list[i] > max:
        max = list[i]
        j = i

print(max, j, sep=' ')
