nk = list(map(int, input().split()))
a = list('I' * nk[0])

for _ in range(nk[1]):
    lr = list(map(int, input().split()))
    for i in range((lr[0] - 1), lr[1]):
        a[i] = '.'

print(''.join(a))
