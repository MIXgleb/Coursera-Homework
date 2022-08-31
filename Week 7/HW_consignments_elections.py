with open('input.txt', 'r', encoding='utf8') as inFile:
    sumV = sumP = 0
    myDict = {}
    for line in inFile:
        line = line.split()
        myDict[' '.join(line[:-1])] = int(line[-1])
        sumV += int(line[-1]) / 450
    for party, voice in myDict.items():
        myDict[party] = [voice, voice / sumV]
        sumP += int(myDict[party][1])
    sortDict = sorted(myDict,
                      key=lambda x: (-(myDict[x][1] % 1), -myDict[x][0]))
    i = 0
    while sumP < 450:
        myDict[sortDict[i]][1] += 1
        sumP += 1
        i += 1
    [print(party, int(voice[1])) for party, voice in myDict.items()]
