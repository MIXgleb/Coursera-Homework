dist = list(map(int, input().split()))
cost = list(map(int, input().split()))
sum = 0

dist.sort()
cost.sort(reverse=True)

for i in range(len(dist)):
    sum += (dist[i] * cost[i])

print(sum)
