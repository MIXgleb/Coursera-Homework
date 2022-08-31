def factorial(n):
    while n != 0:
        return n * factorial(n - 1)
    return 1


sum = 0

for i in range(1, int(input()) + 1):
    sum += factorial(i)

print(sum)
