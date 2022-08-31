n = int(input())
town = list(map(int, input().split()))
m = int(input())
bomb = list(map(int, input().split()))

for _ in range(len(town)):
    town[_] = (town[_], _ + 1)

for __ in range(len(bomb)):
    bomb[__] = (bomb[__], __ + 1)


def sort(a):
    return a[0]


town.sort(key=sort)
bomb.sort(key=sort)

i = 0
reply = ['*'] * n

for house in town:
    while i < len(bomb) - 1 and\
            abs(house[0] - bomb[i + 1][0]) < abs(house[0] - bomb[i][0]):
        i += 1
    reply[house[1] - 1] = bomb[i][1]

print(*reply)
