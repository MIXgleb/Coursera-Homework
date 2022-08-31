with open('input.txt', 'r', encoding='utf8') as inFile:
    s = [[], [], []]

    for line in inFile:
        s[int(line.split()[2]) - 9].append(int(line.split()[3]))

print(sum(s[0]) / len(s[0]), sum(s[1]) / len(s[1]), sum(s[2]) / len(s[2]))
