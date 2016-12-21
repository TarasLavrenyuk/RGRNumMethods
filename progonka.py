import datetime
from matrixoperation import show_matrix
from matrix import *


# def show_matrix(m):
#     for line in m:
#         result_line = ''
#         for elem in line:
#             result = ''
#             current = format(elem, '.2f')
#             result += '    ' + current if current.startswith('-') else '     ' + current
#             result_line += result
#         print result_line


def get_d_array(matrix):
    result = []
    i = 0
    while i < len(matrix) - 1:
        result.append(matrix[i][i + 1])
        i += 1
    return result


def get_c_array(matrix):
    result = []
    i = 0
    while i < len(matrix):
        result.append(matrix[i][i])
        i += 1
    return result


def get_b_array(matrix):
    result = []
    i = 0
    while i < len(matrix) - 1:
        result.append(matrix[i + 1][i])
        i += 1
    return result


def get_tau(b, sigma, c):
    return b*sigma + c


def get_sigma(d, tau):
    return -d/tau


def get_lamda(r, b, lamda, tau):
    return (r - lamda*b)/tau


def progonka(m, bbb):
    b = get_b_array(m)
    c = get_c_array(m)
    d = get_d_array(m)
    tau = 0.0
    sigma = 0.0
    lamda = 0.0
    lamdas = []
    sigmas = []
    i = 0
    while i < len(m):
        print 'Iteration #' + str(i+1)
        if i == 0:
            tau = get_tau(0, 0, c[i]*1.0)
        else:
            tau = get_tau(b[i - 1]*1.0, sigma*1.0, c[i]*1.0)
        print 'Tau: ' + str(tau)

        if i != len(m) - 1:
            sigma = get_sigma(d[i]*1.0, tau*1.0)
            # sigmas.append(sigma)
        print 'Sigma: ' + str(sigma)
        sigmas.append(sigma)

        if i == 0:
            lamda = get_lamda(bbb[i]*1.0, 0, 0, tau*1.0)
        else:
            lamda = get_lamda(bbb[i]*1.0, b[i - 1]*1.0, lamda*1.0, tau*1.0)
        print 'Lamda: ' + str(lamda)
        lamdas.append(lamda)
        i += 1
        print '=============================='
        print '=============================='
    # print lamdas

    answers = []
    i = len(lamdas) - 1
    while i >= 0:
        if i == len(lamdas) - 1:
            x = lamdas[i]
        else:
            x = sigmas[i]*1.0*answers[len(answers) - 1] + lamdas[i]*1.0
        answers.append(x)
        i -= 1

    for ans in answers:
        print ans


m = get_matrix3()
b = get_b3()
start = datetime.datetime.now()
progonka(m, b)
print datetime.datetime.now() - start
