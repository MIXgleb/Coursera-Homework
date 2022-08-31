def height(name, myDict):
    return 0 if name not in myDict else height(myDict[name], myDict) + 1


with open('input.txt') as inFile:
    tree = {}
    for _ in range(int(inFile.readline().strip()) - 1):
        child, parent = inFile.readline().split()
        tree[child] = parent
    [print(man, height(man, tree))
     for man in sorted(tree.keys() | tree.values())]
