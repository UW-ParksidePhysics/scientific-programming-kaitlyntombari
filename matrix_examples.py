import numpy as np


matrix = np.array([[2,3],[7,11]]) # this is matrix A
vector = np.array([[5],[13]]) # this is vector b

print(f'A = {matrix}') # prints matrix A

determinant = np.linalg.det(matrix) # this is the determinant of matrix A
print(f'det(A) = {determinant}')

inverse = np.linalg.inv(matrix) # this is the inverse of matrix A
print(f'A^-1 = {inverse} ')

solution = np.matmul(inverse, vector) 
print(f'x = {solution}')

fast_solution = np.linalg.solve(matrix, vector) # skips determinant and inverse

print(f'x = {fast_solution}')