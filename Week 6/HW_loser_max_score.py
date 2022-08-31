scores = [[], [], []]

with open('input.txt', 'r', encoding='utf8') as inFile:
    for man in inFile:
        mansplt = man.split()
        scores[(int(mansplt[-2])) - 9].append(int(mansplt[-1]))

scores[0].sort(reverse=True)
scores[1].sort(reverse=True)
scores[2].sort(reverse=True)

print(scores[0][scores[0].count(max(scores[0]))],
      scores[1][scores[1].count(max(scores[1]))],
      scores[2][scores[2].count(max(scores[2]))])
