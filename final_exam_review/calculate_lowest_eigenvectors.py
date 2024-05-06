"""Identify eigenvectors with smallest K eigenvalues given input matrix using \
NumPy's eig function.

__Kaitlyn Tombari__
"""

import numpy as np


def calculate_lowest_eigenvectors(square_matrix: np.ndarray, number_of_eigenvectors: \
int = 3) -> tuple:
    """Function used to identify eigenvectors with smallest K eigenvalues when given \
    an input matrix."""
    eigenvalues, eigenvectors = np.linalg.eig(square_matrix)
    eigenvalue_indices = np.argsort(eigenvalues)[:number_of_eigenvectors]
    eigenvalues = eigenvalues[eigenvalue_indices]
    eigenvectors = eigenvectors[:, eigenvalue_indices]
    return eigenvalues, eigenvectors


if __name__ == "__main__":
    square_matrix = np.array([[2, -1], [-1, 2]])
    number_of_eigenvectors = 2
    eigenvalues, eigenvectors = calculate_lowest_eigenvectors(square_matrix, \
    number_of_eigenvectors)
    print(f'Eigenvalues: {eigenvalues}')
    print(f'Eigenvectors: {eigenvectors}')
