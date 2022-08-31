schools = [0] * 99

with open('input.txt', 'r', encoding='utf8') as inFile:
    for man in inFile:
        schools[int(man.split()[-2]) - 1] += 1

for i in range(99):
    if schools[i] == max(schools):
        print(i + 1, end=' ')
