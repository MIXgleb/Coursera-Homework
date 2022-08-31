with open('input.txt') as inFile:
    myDict = {}
    for _ in range(int(inFile.readline())):
        splt = inFile.readline().split()
        word1, word2 = splt[0], splt[1]
        myDict[word1] = word2
        myDict[word2] = word1
    print(myDict[inFile.readline().strip()])
