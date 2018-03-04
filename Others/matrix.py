

def matrix_transpose(matrix):
    Transpose =  zip(*matrix)
    lst = [row for row in Transpose]
    return lst

#print(matrix_transpose([[1,2],[3,4]]))
#print(matrix_transpose(input('Enter a matrix')))

def matrix_det(matrix):
#matrix = [[1,2], [3,4]]
    if len(matrix[0]) != len(matrix):
        print('Cannot calculate determinant of a non-square matrix.')
    elif len(matrix[0])>2 and len(matrix) > 2:
        print('Cannot calculate determinant of a n-by-n matrix", where you substitute n with the dimension of the input matrix.')
    else:
        if len(matrix[0]) == 1 and len(matrix)==1:
            determinent = matrix[0] * matrix[1]
        else:
            determinent= matrix[0][0] *matrix[1][1] - matrix[0][1]*matrix[1][0]
    return determinent

#print(matrix_det([[1,2], [3,4]]))

def matrix_sum(matrix1, matrix2):

    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        print('Cannot calculate sum of a non-symmetrical matrix.')
    else:
        lst = [(matrix1[i][j] + matrix2[i][j]) for i in range(len(matrix1)) for j in range(len(matrix1[0]))]
    return lst

#print(matrix_sum([[1,2], [3,4]],[[5,6], [7,8]] ))

import numpy as np
def matrix_mul(matrix1, matrix2):
    matrix1 = np.array(matrix1)
    matrix2 = np.array(matrix2)
    return (matrix1.dot(matrix2))

def matrix_inv(matrix):
    matrix = np.array(matrix)
    return np.linalg.inv(matrix)
