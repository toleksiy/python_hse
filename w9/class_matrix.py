from sys import stdin
from copy import deepcopy


class Matrix:
    def __init__(self, vardata):
        self.data = deepcopy(vardata)

    def __str__(self):
        strings = str()
        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                strings += (str(self.data[i][j]))
                if j < len(self.data[i]) - 1:
                    strings += '\t'
            if i < len(self.data) - 1:
                strings += '\n'
        return strings

    def size(self):
        return (len(self.data), len(self.data[0]))

exec(stdin.read())
