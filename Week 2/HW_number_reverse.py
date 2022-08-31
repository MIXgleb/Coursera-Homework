n = int(input())

while n != 0:
    i = n % 10
    print(i, end='')
    n //= 10
