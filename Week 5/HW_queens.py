# print('{0:.25f}'.format(0.1))
axisX = []
axisY = []
axisnegativeD = []
axispositiveD = []
i = 0

for _ in range(8):
    xy = list(map(int, input().split()))
    if axisY.count(xy[1]) != 0 or \
       axisX.count(xy[0]) != 0 or \
       axisnegativeD.count(xy[1] - xy[0]) != 0 or \
       axispositiveD.count(xy[0] + xy[1]) != 0:
        i += 1
    axisX.append(xy[0])
    axisY.append(xy[1])
    axisnegativeD.append(xy[1] - xy[0])
    axispositiveD.append(xy[0] + xy[1])

print('NO' if i == 0 else 'YES')
