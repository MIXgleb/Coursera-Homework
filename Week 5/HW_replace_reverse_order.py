# list = list(map(int, input().split()))
# print(' '.join(map(str, list)))


a = list(map(int, input().split()))

for i in range(int(len(a) / 2)):
    a[i], a[-1 - i] = a[-1 - i], a[i]

print(*a)
