parties = []
votes = []
mark = 0

with open('input.txt', 'r', encoding='utf8') as inFile:
    for i in inFile:
        i = i.strip()
        if i == 'VOTES:':
            mark = 1
        if mark == 0 and i != 'PARTIES:':
            parties.append(i)
        elif mark == 1 and i != 'VOTES:':
            votes.append(i)

for j in parties:
    if votes.count(j) / len(votes) * 100 >= 7:
        print(j)
