from sys import stdin
from copy import deepcopy


class MatrixError(BaseException):
    def __init__(self, m1, m2):
        self.matrix1 = m1
        self.matrix2 = m2


class Matrix:
    def __init__(self, m):
        self.matrix = deepcopy(m)

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, line)) for line in self.matrix])

    def size(self):
        return len(self.matrix), len(self.matrix[0])

    def __add__(self, other):
        if self.size() == other.size():
            return Matrix([[(self.matrix[i][j] + other.matrix[i][j])
                            for j in range(self.size()[1])]
                           for i in range(self.size()[0])])
        else:
            raise MatrixError(self, other)

    def __mul__(self, other):
        return Matrix([[self.matrix[i][j] * other
                        for j in range(self.size()[1])]
                       for i in range(self.size()[0])])
    __rmul__ = __mul__

    def transpose(self):
        self.matrix = [[self.matrix[i][j]
                        for i in range(self.size()[0])]
                       for j in range(self.size()[1])]
        return Matrix(self.matrix)

    @staticmethod
    def transposed(other):
        return Matrix([[other.matrix[i][j]
                        for i in range(other.size()[0])]
                       for j in range(other.size()[1])])


exec(stdin.read())
