s = str(input())

pos = s.find(' ')

print(s[pos + 1:], s[0:pos], sep=' ')
