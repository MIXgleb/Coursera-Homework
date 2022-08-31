l1, r1 = int(input()), int(input())
l2, r2 = int(input()), int(input())
l3, r3 = int(input()), int(input())
n, n1, n2, n3 = -1, 1, 2, 3

if l1 > l2:
    l1, r1, n1, l2, r2 = l2, r2, n2, l1, r1
if l1 > l3:
    l1, r1, n1, l3, r3 = l3, r3, n3, l1, r1
if l2 > l3:
    l2, r2, n2, l3, r3, n3 = l3, r3, n3, l2, r2, n2

if (l2 <= r1 and l3 <= r2) or l3 <= r1 or r3 <= r1:
    n = 0
elif 0 < l3 - r2 <= r1 - l1 or r2 >= l3:
    if n1 < n or n == -1:
        n = n1
elif 0 < l2 - r1 <= r3 - l3 or r1 >= r2:
    if l3 - r1 <= r2 - l2 and (n2 < n or n == -1):
        n = n2
    elif n3 < n or n == -1:
        n = n3
print(n)
