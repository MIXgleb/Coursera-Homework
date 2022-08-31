# list = list(map(int, input().split()))
# print(' '.join(map(str, list)))
# print(*list)
list = list(map(int, input().split()))
k = 0

for i in range(len(list)):
    if list[i] > 0:
        k += 1

print(k)
