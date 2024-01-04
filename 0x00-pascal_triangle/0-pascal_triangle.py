#!/usr/bin/python3
"""Pascal Triangle"""


def pascal_triangle(n):
    """
    function:
        n int

    """
    pascal_Tr = []

    if n <= 0:
        return []

    for j in range(n):
        if (j == 0):
            pascal_Tr.append([1])
        else:
            c_row = []
            for i in range(j + 1):
                if (j == i or i == 0):
                    c_row.append(1)
                else:
                    c_row.append(pascal_Tr[j - 1][i - 1] +
                                 pascal_Tr[j - 1][i])

            pascal_Tr.append(c_row)

    return (pascal_Tr)
