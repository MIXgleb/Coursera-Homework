outFile = open('output.txt', 'w', encoding='utf8')
ScoresList = []

with open('input.txt', 'r', encoding='utf8') as inFile:
    k = int(inFile.readline())
    for man in inFile:
        manSplt = man.split()
        scr1 = int(manSplt[-1])
        scr2 = int(manSplt[-2])
        scr3 = int(manSplt[-3])
        if scr3 >= 40 and scr2 >= 40 and scr1 >= 40:
            ScoresList.append(scr3 + scr2 + scr1)

ScoresList.sort(reverse=True)

if k >= len(ScoresList):
    print(0, file=outFile)
elif ScoresList[0] == ScoresList[k]:
    print(1, file=outFile)
else:
    while ScoresList[k - 1] == ScoresList[k]:
        k -= 1
    print(ScoresList[k - 1], file=outFile)

outFile.close()
