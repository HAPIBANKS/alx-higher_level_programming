#!/usr/bin/python3
"""
Divide a matrix by a given integer
"""


def matrix_divided(matrix, div):
    """
    matrix must be a list of lists
    of int or float
    otherwise raise a Typeerror
    Each row of the matrix must be of thesame size
    otherwise, raise a Typeerror
    div can't be zero
    all element of the matrix should be divided by div
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    row_size = len(matrix[0])
    for row in matrix:
        if len(row) != row_size:
            raise TypeError("each row of the matrix must have the same size")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    for row in matrix:
        divided = [round(i / div, 2) for i in row]
        new_matrix.append(divided)

    return new_matrix
