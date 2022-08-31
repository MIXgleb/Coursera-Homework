s = str(input())

pos1 = s.find('h')
pos2 = s[::-1].find('h')

print(s[:(len(s) - pos2 - 1)], s[(pos1 + 1):], sep='')
