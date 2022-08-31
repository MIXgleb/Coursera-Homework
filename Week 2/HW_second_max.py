n = int(input())
max = 0
preMax = 0

while n != 0:
    if n >= max:
        max, preMax = n, max
    if max > n > preMax:
        preMax = n
    n = int(input())

print(preMax)
