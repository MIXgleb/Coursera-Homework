a, b = int(input()), int(input())


def reverse(n):
    return (n % 10) * 10 + n // 10


for i in range(a, b + 1):
    if i // 100 == reverse(i % 100):
        print(i)
