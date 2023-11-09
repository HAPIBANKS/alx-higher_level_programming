#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square_matrix = []
    for row in matrix:
        new_row = []
        for i in row:
            new_row.append(i ** 2)
        square_matrix.append(new_row)
    return square_matrix
