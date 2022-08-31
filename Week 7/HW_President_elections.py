with open('input.txt', 'r', encoding='utf8') as inFile,\
        open('output.txt', 'w', encoding='utf8') as outFile:
    myDict = {}
    people = 0
    for line in inFile:
        myDict[line.strip()] = myDict.get(line.strip(), 0) + 1
        people += 1
    Surname = sorted(myDict, key=lambda x: -myDict[x])
    print(Surname[0], file=outFile) if myDict[Surname[0]] / people > 0.5 \
        else print(Surname[0], Surname[1], sep='\n', file=outFile)
