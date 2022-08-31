# list = list(map(int, input().split()))
# print(' '.join(map(str, list)))
# print(*list)
list = list(map(int, input().split()))
min = 1001

for i in range(len(list)):
    if list[i] > 0 and list[i] < min:
        min = list[i]

print(min)
