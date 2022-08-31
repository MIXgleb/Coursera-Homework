leg = int(input())
a = sorted(list(map(int, input().split())))
k = 0

for i in a:
    if i >= leg:
        k += 1
        leg = i + 3

print(k)
