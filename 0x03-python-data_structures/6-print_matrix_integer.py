#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for val in i:
            if val != 3 and val != 6 and val != 9:
                print("{:d}".format(val), end=" ")
            else:
                print("{:d}".format(val), end="")
        print()
