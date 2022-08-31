a = list(map(int, input().split()))
b = [a[0]]
prev = a[0]

for i in a:
    if i != prev:
        b.append(i)
        prev = i

print(len(b))
