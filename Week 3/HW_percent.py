# print('{0:.25f}'.format(0.1))
# print(float(2**100).as_integer_ratio())

p = float(input())
x = int(input())
y = int(input())

cent = (y * (1 + p / 100) + x * (1 + p / 100) * 100 % 100)
rub = x * (1 + p / 100) + cent // 100

print(int(rub), int(cent % 100))
