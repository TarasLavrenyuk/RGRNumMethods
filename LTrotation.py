from matrix import *
import math


def get_matrix_dimension(matrix):
    n = len(matrix)
    return n - 1


def get_Cij(matrix, i, j):
    Cij = matrix[i][i] / math.sqrt(math.pow(matrix[i][i], 2) + math.pow(matrix[i][j], 2))
    return Cij


def get_Sij(matrix, i, j):
    Sij = matrix[i][j] / math.sqrt(math.pow(matrix[i][i], 2) + math.pow(matrix[i][j], 2))
    return Sij


def get_single_matrix(N):
    row = []
    rows = []
    i = 0
    while i <= N:
        row.append(0)
        i += 1
    i = 0
    while i <= N:
        a = row[:]
        a[i] = 1
        rows.append(a)
        i += 1
    return rows


def get_zero_matrix(N):
    row = []
    rows = []
    i = 0
    while i <= N:
        row.append(0)
        i += 1
    i = 0
    while i <= N:
        rows.append(row[:])
        i += 1
    return rows


def print_matrix(matrix):
    for row in matrix:
        print row


def multiplicate_matrix(A, B):
    result = get_zero_matrix(get_matrix_dimension(A))
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result


def delimeter():
    print '=============================='


def specify_numbers(matrix):
    i = 0
    while i < len(matrix):
        j = 0
        while j < len(matrix[i]):
            if math.fabs(matrix[i][j]) < 10**-10:
                matrix[i][j] = 0
            j += 1
        i += 1
    return matrix


def get_Y_array(L, b):
    y = []
    k = 0
    while k < len(L):
        y.append([0])
        suma = 0
        j = 0
        if k - 1 >= j:
            while j <= k - 1:
                suma += L[k][j] * y[j][0]
                j += 1
        y[k][0] = (b[k] - suma) / L[k][k]
        k += 1
    return y


def get_T_transponovana(T_array):
    Tt = T_array[0]
    i = 1
    while i < len(T_array):
        Tt = multiplicate_matrix(Tt, T_array[i])
        i += 1
    return Tt


def get_det(L):
    detL = L[0][0]
    i = 1
    while i < len(L):
        detL = detL * L[i][i]
        i += 1
    return detL


def LT_rotation(matrix):
    N = get_matrix_dimension(matrix)
    T_arrays = []
    iteration = 1
    i = 0
    A = matrix
    while i < N:
        j = i + 1
        while j <= N:
            delimeter()
            print 'Iteration #' + str(iteration) + ':'
            Cij = get_Cij(A, i, j)
            Sij = get_Sij(A, i, j)
            T = get_single_matrix(N)
            T[i][i] = Cij
            T[j][j] = Cij
            T[i][j] = -Sij
            T[j][i] = Sij
            T_arrays.append(T)
            specify_numbers(T)
            print 'Matrix T' + str(i+1) + str(j+1)
            print_matrix(T)
            A = multiplicate_matrix(A, T)
            specify_numbers(A)
            print 'Matrix A(' + str(iteration) + '):'
            print_matrix(A)
            iteration += 1
            j += 1
            delimeter()
        i += 1
    L = A
    specify_numbers(L)
    print 'Matrix L:'
    print_matrix(L)
    delimeter()
    print 'Y array: '
    print get_Y_array(L, get_b1())
    delimeter()
    print 'T transponovana:'
    print_matrix(get_T_transponovana(T_arrays))
    delimeter()
    print 'Result'
    print_matrix(multiplicate_matrix(get_T_transponovana(T_arrays), get_Y_array(L, get_b1())))
    print 'Determinant A:'
    print get_det(L)


LT_rotation(get_matrix1())