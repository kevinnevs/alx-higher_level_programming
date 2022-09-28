#!/usr/bin/python3
"""
pascal_triangle
"""


def pascal_triangle(n):
    """
    returns a list of lists of integers
    representing the Pascal's triangle of n
    """

    if n <= 0:
        return []

    res = []
    for elem in range(n):
        if elem == 0:
            res.append([1])
            continue
        if elem == 1:
            res.append([1, 1])
            continue
        row = []
        for item in range(elem + 1):
            row.append(item)
        for item in range(1, elem):
            row[0] = 1
            row[elem] = 1
            row[item] = res[elem - 1][item] + res[elem - 1][item - 1]
        res.append(row)

    return res
