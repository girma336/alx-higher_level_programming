#!/usr/bin/python3
"""pascal Triangle"""


def pascal_triangle(n):
    """return alist of intager"""

    if n <= 0:
        return []

    triangle = [[1]]

    while len(triangle) != n:
        tri = triangle[-1]
        tmp = [1]
        for i in range(len(tri) - 1):
            tmp.append(tri[i] + tri[i + 1])
        tmp.append(1)
        triangle.append(tmp)
    return triangle
