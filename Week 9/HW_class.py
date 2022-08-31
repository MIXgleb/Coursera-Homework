from sys import stdin
from copy import deepcopy


class Matrix:
    def __init__(self, m):
        self.matrix = deepcopy(m)

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, line)) for line in self.matrix])

    def size(self):
        return len(self.matrix), len(self.matrix[0])


exec(stdin.read())
