a = list(map(int, input().split()))
n = int(input())
i = 0

while i <= len(a) - 1 and n <= a[i]:
    i += 1
print(i + 1)
