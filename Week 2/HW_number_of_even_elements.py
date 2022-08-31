n = 1
i = 0

while n != 0:
    n = int(input())
    if n % 2 == 1 or n == 0:
        continue
    i += 1

print(i)
