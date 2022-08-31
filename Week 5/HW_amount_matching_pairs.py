a = list(map(int, input().split()))
num = 0

for i in a:
    num += a.count(i) - 1

print(num // 2)
