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
        if isinstance(other, int) or isinstance(other, float):
            return Matrix([[self.matrix[i][j] * other
                            for j in range(self.size()[1])]
                           for i in range(self.size()[0])])
        elif isinstance(other, Matrix):
            if self.size()[1] != other.size()[0]:
                raise MatrixError(self, other)
            elif self.size()[1] == other.size()[0]:
                matr = []
                result = []
                s = 0
                for i in range(self.size()[0]):
                    for k in range(other.size()[1]):
                        for j in range(other.size()[0]):
                            s += self.matrix[i][j] * other.matrix[j][k]
                        matr.append(s)
                        s = 0
                    result.append(matr)
                    matr = []
                return Matrix(result)

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

    def det2(self):
        return self.matrix[0][0] * self.matrix[1][1] - \
               self.matrix[0][1] * self.matrix[1][0]

    def detMore2(self):
        det = 0
        if len(self.matrix[0]) == 2:
            return self.det2()
        else:
            for i in range(self.size()[1]):
                Aij = deepcopy(self.matrix[1:])
                [Aij[j].pop(i) for j in range(len(Aij))]
                det += (-1) ** i * self.matrix[0][i] * Matrix(Aij).detMore2()
        return det

    def solve(self, vector):
        if self.size()[0] != self.size()[1]:
            raise Exception('The matrix is not square!')
        elif self.size()[0] != len(vector):
            raise Exception('The matrix and vector have different length!')
        solve = []
        mainDet = self.detMore2()
        for i in range(self.size()[0]):
            KramMatrix = deepcopy(self.matrix)
            for j in range(self.size()[1]):
                KramMatrix[j][i] = vector[j]
            solve.append(Matrix(KramMatrix).detMore2() / mainDet)
        return solve


class SquareMatrix(Matrix):
    def identity(self):
        return SquareMatrix([[1 if i == j else 0
                              for j in range(self.size()[0])]
                             for i in range(self.size()[0])])

    def __pow__(self, power):
        if power == 0:
            return self.identity()
        elif power % 2 == 0:
            matr = SquareMatrix((self * self).matrix)
            return matr**(power // 2)
        else:
            return self * (self**(power - 1))


exec(stdin.read())
