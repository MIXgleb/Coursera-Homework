n = int(input())
max = 0
i = 1

while n != 0:
    if n > max:
        max = n
        i = 1
    elif n == max:
        i += 1
    n = int(input())

print(i)
