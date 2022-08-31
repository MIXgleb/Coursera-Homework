def changeNumber(number):
    numberList = []
    for digit in number:
        if digit.isdigit():
            numberList.append(int(digit))
    if len(numberList) == 7:
        numberList = [8, 4, 9, 5] + numberList
    return numberList[1:]


addNumber = changeNumber(input())

[print('YES') if changeNumber(input()) == addNumber
    else print('NO') for _ in range(3)]
