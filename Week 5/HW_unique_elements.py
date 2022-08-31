a = list(map(int, input().split()))

print(*[a[i] for i in range(len(a)) if a.count(a[i]) == 1])
