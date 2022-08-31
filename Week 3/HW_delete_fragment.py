s = str(input())

pos1 = s.find('h')
pos2 = s[::-1].find('h')

print(s[:(pos1)] + s[(len(s) - pos2):])
