from sys import stdin
from copy import deepcopy


class Matrix:
    def __init__(self, m):
        self.matrix = deepcopy(m)

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, line)) for line in self.matrix])

    def size(self):
        return len(self.matrix), len(self.matrix[0])

    def __add__(self, other):
        return Matrix([[(self.matrix[i][j] + other.matrix[i][j])
                        for j in range(self.size()[1])]
                       for i in range(self.size()[0])])

    def __mul__(self, other):
        return Matrix([[self.matrix[i][j] * other
                        for j in range(self.size()[1])]
                       for i in range(self.size()[0])])

    __rmul__ = __mul__


exec(stdin.read())
