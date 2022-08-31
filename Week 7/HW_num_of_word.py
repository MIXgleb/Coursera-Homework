with open('input.txt') as inFile:
    myDict = {}
    for word in inFile.read().split():
        print(myDict[word], end=' ') if word in myDict \
            else print(0, end=' ')
        myDict[word] = myDict.get(word, 0) + 1
