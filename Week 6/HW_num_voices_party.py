parties = []
votes = []
mark = 0

with open('input.txt', 'r', encoding='utf8') as inFile:
    for i in inFile:
        i = i.strip()
        if i == 'VOTES:':
            mark = 1
        if mark == 0 and i != 'PARTIES:':
            parties.append([0, i])
        elif mark == 1 and i != 'VOTES:':
            votes.append(i)

for i in parties:
    i[0] = votes.count(i[1])

parties.sort(key=lambda n: (-n[0], n[1]))

for i in parties:
    print(i[1])
