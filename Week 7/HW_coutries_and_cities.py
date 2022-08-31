with open('input.txt') as inFile:
    myDict = {}
    for i in range(int(inFile.readline())):
        splt = inFile.readline().split()
        country, cities = splt[0], splt[-1:0:-1]
        for city in cities:
            myDict[city] = country
    [print(myDict[inFile.readline().strip()])
     for _ in range(int(inFile.readline()))]
