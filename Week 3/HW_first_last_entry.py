s = str(input())

pos = s.find('f')
posRev = s[::-1].find('f')

if pos == posRev == -1:
    print('')
elif pos == (len(s) - posRev - 1):
    print(pos)
elif pos != (len(s) - posRev - 1):
    print(pos, len(s) - posRev - 1)
