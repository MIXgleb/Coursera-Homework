a = list(map(int, input().split()))
maxNum = 0

for i in a:
    if a.count(i) > maxNum:
        maxNum = a.count(i)
        num = i

print(num)
