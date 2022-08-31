n = int(input())
if n % 10 == 1 and not n == 11:
    print(n, 'korova')
elif n % 10 in [2, 3, 4] and n not in [12, 13, 14]:
    print(n, 'korovy')
elif n % 10 in [5, 6, 7, 8, 9, 0] or n in [11, 12, 13, 14]:
    print(n, 'korov')
