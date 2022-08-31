with open('input.txt') as inFile:
    myDict = {}
    for word in inFile.read().split():
        myDict[word] = myDict.get(word, 0) + 1
    print(sorted(myDict, key=lambda x: (-myDict[x], x))[0])
