# print('{0:.25f}'.format(0.1))
# print(float(2**100).as_integer_ratio())

n = float(input())
frac = '{0:.2f}'.format(n - int(n))

print(int(n // 1), int(float(frac) * 100), end=' ')
