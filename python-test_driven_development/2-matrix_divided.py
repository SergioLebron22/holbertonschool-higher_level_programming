#!/usr/bin/python3

"""
This file contains the function matric divide
"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a given divisor.

    Args:
        matrix (list): A matrix represented as a list 
        of lists containing integers or floats.
        div (int or float): The divisor.

    Raises:
        ZeroDivisionError: If the divisor is zero.
        TypeError: If the divisor is not a number 
        or if the matrix is not a valid matrix.

    Returns:
        list: A new matrix with the elements divided by 
        the divisor, rounded to 2 decimal places.
    """

    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    new_matrix = []
    for row in matrix:
        if not isinstance(matrix, list) or not isinstance(row, list):
            raise TypeError("matrix must be a matrix\
                        (list of lists) of integers/floats")

        row_len = len(matrix[0])
        if len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")
        for num in row:
            if not isinstance(num, (int, float)):
                raise TypeError("matrix must be a matrix\
                        (list of lists) of integers/floats")   
            new_matrix.append(round(num / div, 2))

    return new_matrix
