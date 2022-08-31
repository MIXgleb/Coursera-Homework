nk = list(map(int, input().split()))
strikes = set()
weekends = set(range(6, nk[0] + 1, 7)) | set(range(7, nk[0] + 1, 7))

for _ in range(nk[1]):
    days = list(map(int, input().split()))
    strikes |= set(range(days[0], nk[0] + 1, days[1]))

print(len(strikes - weekends))
