# print('{0:.25f}'.format(0.1))
# print(float(2**100).as_integer_ratio())

n = int(input())
i = 1
sum = 0

while i <= n:
    sum += 1 / i**2
    i += 1

print(sum)
