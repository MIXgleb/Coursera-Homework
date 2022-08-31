s = str(input())
frag = ''
i = 0
while i < len(s):
    if i % 3 != 0:
        frag += s[i:i+1]
    i += 1

print(frag)
