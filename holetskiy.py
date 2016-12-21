import datetime

import matrixoperation as mr
import math
from matrix import get_matrix2

def solve_quad(m):
    matrix_len = len(m)
    u = [[0] * (matrix_len) for i in range(matrix_len)]

    def formUmatrix():
        for i in range(matrix_len):
            # print 'IIII: ', i
            for j in range(i, matrix_len):
                # print ': ', j
                if i == j:
                    u[i][j] = math.sqrt(m[i][j] - sum([u[ii][i] ** 2 for ii in range(i)]))
                else:
                    u[i][j] = (m[i][j] - sum(u[k][i] * u[k][j] for k in range(i))) / u[i][i]

    def determinant(matr):
        return (reduce(lambda x, y: x * y, [matr[i][i] for i in range(len(matr))]) ** 2)

    def obernenaA(u):
        aober = [[0] * (len(u)) for i in range(len(u))]

        def Ti(i, j):
            if i == j:
                return 1 / u[i][i]
            else:
                return -1 * (sum([u[i][k] * Ti(k, j) for k in range(i + 1, j)])) / u[i][j]

        for r in range(len(u)):
            for s in range(r, len(u)):
                aober[r][s] = sum(Ti(r, k) * Ti(s, k) for k in range(s, len(u)))
                # print 'r: ', r, 's: ', s
                # print aober[r][s]

        return aober

    formUmatrix()
    transponed = mr.transpone(u)
    determinator = determinant(u)
    obernenaQuad = obernenaA(u)
    # mr.show_matrix(transponed)
    # adding columns

    for i in range(matrix_len):
        transponed[i].append(matrix[i][matrix_len])



    result = mr.solveDownTriangle(transponed)

    for i in range(matrix_len):
        u[i].append(result[i])

    result = mr.solveUpperTriangle(u)
    print '=============================================='
    for r in result:
        print r
    print '=============================================='


    return result, determinator, obernenaQuad


matrix = get_matrix2()
# mr.show_matrix(matrix)
start = datetime.datetime.now()
res, determinantor, obernenaQuad = solve_quad(matrix)
print datetime.datetime.now() - start
print 'Answer: ', res
print 'Determinant: ', determinantor
print 'Obernena matriza:'
print mr.show_matrix(obernenaQuad)
