with open('input.txt', 'r', encoding='utf8') as inFile:
    text = inFile.read().split()

print(len(set(text)))
