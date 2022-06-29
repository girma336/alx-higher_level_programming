#!/usr/bin/python3
"""Matrix division"""


def matrix_divided(matrix, div):
    """Divides every element of a matrix
    Args:
        matrix (list): A list of lists of integers
        or floats div (int/float): The divisor.
    """

    if div == float('inf') or div == -float('inf') or div != div:
        div = 10
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    return [[round(item / div, 2) for item in row] for row in matrix]
