# print('{0:.25f}'.format(0.1))
# print(float(2**100).as_integer_ratio())

a = float(input())
b = float(input())
c = float(input())

p = (a + b + c) / 2
s = (p * (p - a) * (p - b) * (p - c))**0.5

print('{0:.6f}'.format(s))
