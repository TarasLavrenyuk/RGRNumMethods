import datetime

from matrix import get_matrix_1_full
from matrix import get_matrix2
from matrixoperation import show_matrix

from pprint import pprint


class Lu:
    rowCount = 0
    colCount = 0
    det = 1
    # matrix = get_matrix_1_full()
    matrix = get_matrix2()
    answer = [0]

    def __init__(self, row_cnt, col_cnt):
        self.rowCount = row_cnt
        self.colCount = col_cnt
        self.answer *= col_cnt

    def show(self):
        pprint(self.matrix, width=19)

    def solve(self):
        for p in xrange(self.rowCount):
            j = p
            for z in xrange(j, self.rowCount):
                for k in xrange(j):
                    self.matrix[z][j] -= self.matrix[k][j] * self.matrix[z][k] * 1.0

            i = p
            for z in xrange(i+1, self.rowCount + 1):
                for k in xrange(0, i):
                    self.matrix[i][z] -= self.matrix[k][z] * self.matrix[i][k] * 1.0
                self.matrix[i][z] /= self.matrix[i][i] * 1.0

        for z in xrange(self.rowCount - 1, -1, -1):
            self.answer[z] = self.matrix[z][self.rowCount]
            for k in xrange(z + 1, self.rowCount):
                self.answer[z] -= self.matrix[z][k] * self.answer[k] * 1.0

        print 'Matrix'
        show_matrix(self.matrix)

        print "Answer: "
        for ans in self.answer:
            print ans

        for q in xrange(0, self.rowCount):
            self.det *= self.matrix[q][q] * 1.0
        print "Determinant: "
        print self.det

    def obernena(self):
        b = [[0 for x in range(self.rowCount)] for y in range(self.colCount)]
        for p in xrange(self.rowCount - 1, -1, -1):
            i = p
            for z in xrange(i, -1, -1):
                if i == z:
                    b[i][z] = 1
                else:
                    b[i][z] = 0

                for k in xrange(z + 1, self.rowCount):
                    b[i][z] -= b[i][k] * self.matrix[k][z] * 1.0
                b[i][z] /= self.matrix[z][z] * 1.0
            j = p
            for z in xrange(j - 1, -1, -1):
                for k in xrange(z + 1, self.rowCount):
                    b[z][j] += b[k][j] * self.matrix[z][k]  * 1.0
                b[z][j] = b[z][j] * (-1)

        print b


if __name__ == "__main__":
    start = datetime.datetime.now()
    # met = Lu(9, 9)
    met = Lu(10, 10)
    met.solve()
    print datetime.datetime.now() - start
    met.obernena()



