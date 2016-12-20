def show_matrix(m):
    for line in m:
        result_line = ''
        for elem in line:
            result = ''
            current = format(elem, '.5f')
            result += '    ' + current if current.startswith('-') else '     ' + current
            result_line += result
        print result_line

    print "\n"


def transpone(m):
    matrix_len = len(m)
    u = [[0] * matrix_len for i in range(matrix_len)]
    for i in range(matrix_len):
        for j in range(matrix_len):
            u[i][j] = m[j][i]
    return u


def func(m):
    matrix_length = len(m)
    x = [0 for i in range(matrix_length)]
    for k in range(matrix_length - 1, -1, -1):
        x[k] = (m[k][-1] - sum([m[k][j] * x[j] for j in range(k + 1, matrix_length)])) / m[k][k]


def multiply(m, mm):
    leng = len(m)
    u = [[0] * leng for i in range(leng)]
    for i in range(leng):
        for j in range(leng):
            u[i][j] = sum(m[i][r] * mm[r][j] for r in range(leng))
    return u


def solveUpperTriangle(m):
    matrix_length = len(m)
    x = [0 for i in range(matrix_length)]
    for k in range(matrix_length - 1, -1, -1):
        x[k] = (m[k][-1] - sum([m[k][j] * x[j] for j in range(k + 1, matrix_length)])) / m[k][k]
    return x


def solveDownTriangle(m):
    matrix_length = len(m)
    y = [0 for i in range(matrix_length)]
    for i in range(matrix_length):
        y[i] = (m[i][-1] - sum([m[i][j] * y[j] for j in range(i)])) / m[i][i]
    return y