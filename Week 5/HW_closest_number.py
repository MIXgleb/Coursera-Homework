n = int(input())
a = list(map(int, input().split()))
x = int(input())
b = a[0]

for i in a:
    if abs(i - x) < abs(x - b):
        b = i

print(b)
