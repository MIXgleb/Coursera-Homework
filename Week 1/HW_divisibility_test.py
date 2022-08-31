a = int(input())
b = int(input())
print('YES' * 0 ** (a % b) + 'NO' * (1 - 0 ** (a % b)))
