n = int(input())
s, m = 0, 0

for j in range(n + 1):
    m += j

for i in range(n - 1):
    s += int(input())

print(m - s)
