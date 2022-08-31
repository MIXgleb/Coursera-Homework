stations = list(map(int, input().split()))
bus1 = sorted(stations[:2])
bus2 = sorted((stations[2:]))

print(len(set(range(bus1[0], bus1[1] + 1)) & set(range(bus2[0], bus2[1] + 1))))
