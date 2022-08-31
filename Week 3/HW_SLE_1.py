# print('{0:.25f}'.format(0.1))
# print(float(2**100).as_integer_ratio())

a, b, c, d, e, f = (float(input()) for _ in range(6))

det = a * d - b * c
detX = e * d - b * f
detY = a * f - e * c

print(detX/det, detY/det)
