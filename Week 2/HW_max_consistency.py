n = int(input())
maxNum = n

while n != 0:
    if n > maxNum and n != 0:
        maxNum = n
    n = int(input())

print(maxNum)
