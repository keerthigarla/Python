import numpy as np
def matrix_mul(matrix1, matrix2):
    return (matrix1.dot(matrix2))

def matrix_inv(matrix):
    return np.linalg.inv(matrix)
#print('Multiply', matrix_mul([[ 5, 1 ,3], [ 1, 1 ,1], [ 1, 2 ,1]],  [[1, 2, 3]]))
#print('Inverse', matrix.inv([[ 5, 1 ,3], [ 1, 1 ,1], [ 1, 2 ,1]]))
matrix1 = np.array([[ 5, 1 ,3], [ 1, 1 ,1], [ 1, 2 ,1]])
matrix2 = np.array([[ 5, 1 ,3], [ 1, 1 ,1], [ 1, 2 ,1]])
print(matrix1.dot(matrix2))
print(np.linalg.inv(matrix1))
