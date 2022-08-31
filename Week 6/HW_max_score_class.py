with open('input.txt', 'r', encoding='utf-8') as inFile:
    scores = [[], [], []]
    for man in inFile:
        scores[int(man.split()[2]) - 9].append(int(man.split()[3]))

print(max(scores[0]), max(scores[1]), max(scores[2]))
