mySet = set(range(1, int(input()) + 1))
data = input()

while str(data) != 'HELP':
    ques = str(input())
    if ques == 'YES':
        mySet &= set(map(int, data.split()))
    elif ques == 'NO':
        mySet -= set(map(int, data.split()))
    data = input()

print(*sorted(mySet))
