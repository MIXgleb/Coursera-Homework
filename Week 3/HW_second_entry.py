s = str(input())

pos1 = s.find('f')

if pos1 == -1:
    print(-2)
elif s.find('f', pos1 + 1) == -1:
    print(-1)
else:
    print(s.find('f', pos1 + 1))
