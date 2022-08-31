sn = list(map(int, input().split()))
a = sorted(list([int(input()) for _ in range(sn[1])]))
sum = 0
j = 0

for i in a:
    sum += i
    if sum <= sn[0]:
        j += 1

print(j)
