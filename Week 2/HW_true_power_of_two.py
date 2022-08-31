n = int(input())
i = 1

while i <= n:
    if n == i:
        print("YES")
        break
    i = i * 2

if i > n:
    print("NO")
