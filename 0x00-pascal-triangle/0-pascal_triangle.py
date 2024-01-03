#!/usr/bin/python3
"""
0-pascal_triangle.py
"""



def pascal_triangle(n):
    """
    this function returns a list of lists of integers,
    representing the Pascal’s triangle of n.
    """
    if n <= 0:
        return []

    triangles = []
    for i in range(n):
        r = [1] * (i + 1)
        if i >= 2:
            for j in range(1, i):
                r[j] = triangles[i - 1][j - 1] + triangles[i - 1][j]
        triangles.append(r)
    return triangles

