nm = list(map(int, input().split()))
anya = set([input() for _ in range(nm[0])])
borya = set([input() for _ in range(nm[1])])
intrsctn = anya & borya
anya -= intrsctn
borya -= intrsctn

print(len(intrsctn))
print(*sorted(map(int, intrsctn)))
print(len(anya))
print(*sorted(map(int, anya)))
print(len(borya))
print(*sorted(map(int, borya)))
