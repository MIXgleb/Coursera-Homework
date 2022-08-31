# print('{0:.25f}'.format(0.1))
# print(float(2**100).as_integer_ratio())

p = float(input())
x = float(input())
y = float(input())
k = float(input())
i = 0

z = x * 100 + y
while i < k:
    z += int(z * (p / 100))
    i += 1

print(int(z // 100), int(z % 100))
