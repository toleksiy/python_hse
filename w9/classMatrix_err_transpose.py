from sys import stdin
from copy import deepcopy


class MatrixError(BaseException):
    def __init__(self, object, other):
        self.matrix1 = object
        self.matrix2 = other


class Matrix:
    @staticmethod
    def transposed(obj):
        return Matrix([[obj.arr[j][i] for j in range(len(obj.arr))]
                       for i in range(len(obj.arr[0]))])

    def __init__(self, arr):
        self.arr = deepcopy(arr)

    def __str__(self):
        return '\n'.join('\t'.join(map(str, line)) for line in self.arr)

    def __add__(self, other):
        if len(self.arr) == len(other.arr):
            return Matrix([[self.arr[i][j]+other.arr[i][j]
                            for j in range(len(self.arr[0]))]
                           for i in range(len(self.arr))])
        else:
            raise MatrixError(self, other)

    def __mul__(self, other):
        mas = [[j * other for j in i] for i in self.arr]
        self.mas = mas
        return Matrix(self.mas)

    __rmul__ = __mul__

    def transpose(self):
        self.arr = [[self.arr[j][i] for j in range(len(self.arr))]
                    for i in range(len(self.arr[0]))]
        return Matrix(self.arr)

    def size(self):
        return (len(self.arr), len(self.arr[0]))


exec(stdin.read())
