with open('input.txt', 'r', encoding='utf-8') as inFile:
    score = [[], [], []]
    for man in inFile:
        score[int(man.split()[2]) - 9].append(int(man.split()[3]))

print(score[0].count(max(score[0])),
      score[1].count(max(score[1])),
      score[2].count(max(score[2])))
