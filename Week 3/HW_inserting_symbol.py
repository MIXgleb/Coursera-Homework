s = str(input())
pos = 1
frag = s[0:1]

while pos < len(s):
    frag = frag + '*' + s[pos:pos + 1]
    pos += 1

print(frag)
