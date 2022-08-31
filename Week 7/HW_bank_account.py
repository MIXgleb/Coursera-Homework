with open('input.txt') as inFile:
    account = {}
    for line in inFile:
        line = line.split()
        if line[0] == 'DEPOSIT':
            account[line[1]] = account.get(line[1], 0) + int(line[2])
        elif line[0] == 'WITHDRAW':
            account[line[1]] = account.get(line[1], 0) - int(line[2])
        elif line[0] == 'BALANCE':
            print(account[line[1]]) if line[1] in account else print('ERROR')
        elif line[0] == 'TRANSFER':
            account[line[1]] = account.get(line[1], 0) - int(line[3])
            account[line[2]] = account.get(line[2], 0) + int(line[3])
        elif line[0] == 'INCOME':
            p = int(line[1]) / 100
            for client, check in account.items():
                account[client] += int(p * check) if check > 0 else 0
