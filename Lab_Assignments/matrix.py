import numpy as np

def generate_matrix(row, col):
    return np.random.randint(1, 10, size=(row, col))

def add_matrices(matrix1, matrix2):
    return np.add(matrix1, matrix2)

def subtract_matrices(matrix1, matrix2):
    return np.subtract(matrix1, matrix2)

def multiply_matrices(matrix1, matrix2):
    return np.matmul(matrix1, matrix2)

