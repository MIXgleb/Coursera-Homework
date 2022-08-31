n = int(input())
set1 = set(input() for _ in range(int(input())))
interSet = set1.copy()

for _ in range(n - 1):
    mset = set(input() for _ in range(int(input())))
    set1 |= mset
    interSet &= mset

print(len(interSet), *interSet, len(set1), *set1, sep='\n')
