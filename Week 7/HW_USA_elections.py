with open('input.txt') as inFile:
    myDict = {}
    for line in inFile:
        line = line.split()
        surname, voices = line[0], int(line[1])
        myDict[surname] = myDict.get(surname, 0) + voices
    [print(man, myDict[man]) for man in sorted(myDict)]
