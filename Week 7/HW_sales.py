with open('input.txt') as inFile:
    buyers = {}
    for line in inFile:
        man, goods, num = line.split()
        buyers[man] = buyers.get(man, {})
        buyers[man][goods] = buyers[man].get(goods, 0) + int(num)
    for man in sorted(buyers):
        print(man, ':', sep='')
        [print(good, num) for good, num in sorted(buyers[man].items())]
