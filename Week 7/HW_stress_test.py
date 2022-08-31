with open('input.txt') as inFile:
    myDict, textPetya = {}, []
    mistake = 0
    for _ in range(int(inFile.readline().strip())):
        strp = inFile.readline().strip()
        myDict[strp.lower()] = myDict.get(strp.lower(), '') + strp + ' '
    for word in inFile.readline().split():
        textPetya = (word.lower(), [i for i in word if i.isupper()])
        if (textPetya[0] not in myDict and
            len(textPetya[1]) != 1) \
                or (textPetya[0] in myDict and
                    word not in myDict[textPetya[0]]):
            mistake += 1
    print(mistake)
