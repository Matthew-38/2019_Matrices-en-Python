#!/usr/bin/python
from functools import reduce # only in Python 3

class Matrix(object):
    """A matrix object. Takes one input variable at creation: a tuple of tuples or list of lists.
    ((,)) is an empty matrix. Otherwise ((1,2),(3,4)) is a 2X2 matrix where 1,2 are in the first column
    All methods return a new Matrix object. Matrices are immutable."""

    def __init__(self, data=()):
        """:type data: tuple of tuples or list of lists"""
        self.emptyMatrix = False
        # Rigorous testing of types and dimensions to be sure we can work with the data given.
        if type(data) not in [tuple, list]:
            raise TypeError("The input data was not in the form of a tuple or list")
        elif len(data) == 0 or (len(data) == 1 and (type(data[0]) in [tuple, list] and len(data[0]) == 0)):  # empty matrix
            self.emptyMatrix = True
            self.matrix = (())
        elif type(data[0]) in [tuple, list]:  # ideal input
            tempi = []
            for i in data:
                if len(i) != len(data[0]):  # test to make sure no missing values!
                    raise ValueError("Matrix has inconsistencies in column lengths or missing values")
                if type(i) != type(data[0]):
                    raise TypeError("Inconsistent data types in matrix input")
                tempj = []
                for j in i:
                    if type(j) not in [int, float]:
                        raise ValueError("The value at position "+i+", "+j+"is not a float or integer")
                    tempj.append(j)
                tempi.append(tuple(tempj))
            self.matrix = tuple(tempi)
        elif type(data[0]) in [int, float]:
            temp = []
            for i in data:
                if type(i) != type(data[0]):
                    raise TypeError('Inconsistent data types in matrix input')
                temp.append((i,))
            self.matrix = tuple(temp)
        else:
            print("Code contains a bug, should not have arrived here")
        self.order = (len(self.matrix[0]), len(self.matrix))  # order is row, column

    def __get__(self) -> tuple:
        return self.matrix

    def stringify(self):
        strout = "("
        for i in range(len(self.matrix[0])):
            for j in range(len(self.matrix)):
                strout += str(self.matrix[j][i])+", "
            strout = strout[:-2]+"\n "  # [:-2] is to remove the trailing comma and space
        return strout[:-2]+")\n"

    def print(self):
        if self.emptyMatrix:
            print("Empty Matrix")
        else:
            print(self.stringify())

    @classmethod
    def __add(cls, a, b): return a+b

    @classmethod
    def __multiply(cls, a, b): return a*b

    @classmethod
    def __divide(cls,a,b): return a/b

    def __perform_scalar_operation(self, func, x):
        return Matrix(tuple(map(lambda matrix: tuple(map(lambda tup: func(tup, x), matrix)), self.matrix)))

    def scalar_add(self, x):
        return self.__perform_scalar_operation(self.__add, x)  # In maths, this doesn't have much sense,
        # but I add it anyway

    def scalar_multiply(self, x):
        return self.__perform_scalar_operation(self.__multiply, x)

    def scalar_divide(self, x):
        return self.__perform_scalar_operation(self.__divide, x)

    def matrix_add(self, other=()):
        if self.order == other.order:
            return Matrix(tuple(map(lambda a, b: tuple(map(lambda x, y: x+y, a, b)), self.matrix, other.matrix)))
            # Here we are doing a map of a map in order to get the elements of the inner tuples
        else:
            raise ValueError("Error, attempting to add matrices of different orders")

    def transpose(self):
        temp = [[] for a in range(self.order[0])]  # initialise list with empty lists as many as there are columns normally
        for i in range(self.order[1]):
            for j in range(self.order[0]):
                temp[j].append(self.matrix[i][j])
        return Matrix(temp)

    def matrix_multiply(self, other=()):
        if self.order[1] == other.order[0]:
            A = self.transpose().matrix  # Use inverted matrix rows and columns for easier manipulation
            B = other.matrix
            temp = []
            for finalRow in range(len(A)):
                temp_inner = []
                for finalCol in range(len(B)):
                    temp_inner.append(sum(a*b for a,b in zip(A[finalRow], B[finalCol])))
                    # temp_inner.append(reduce(lambda a, b: a * b, A[finalRow], B[finalCol]))  # This does NOT work. An example of where NOT to use reduce. The result is not reduced, but super super increased!
                temp.append(temp_inner)
            return Matrix(temp).transpose()
        else:
            raise ValueError("Error, attempting to multiply matrices where the number of columns in the first is not equal to the number of rows in the second. Maybe you got the argument order mixed up?")


if __name__ == "__main__":
    myMatrix = Matrix(((2, 3, 5), (2, 4, 6)))
    print("-----Elementary tests-----")
    myMatrix.print()
    myMatrix.scalar_multiply(4).print()
    myMatrix.matrix_add(myMatrix).print()
    myMatrix.transpose().print()
    print("-----multiplication tests------")
    matrixA = Matrix(((4, 2), (7, 3), (6, 1)))
    matrixB = Matrix(((8, 5, 9),))  # Column matrix
    matrixA.matrix_multiply(matrixB).print()
    matrixC = Matrix(((2, 4), (3, 6), (5, 0), (1, 7)))
    matrixD = Matrix(((3, 4, 2, 9),))
    matrixC.matrix_multiply(matrixD).print()

