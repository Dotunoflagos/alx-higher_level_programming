#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    i = 0
    out = []
    final = []
    while i < len(matrix):
        for j in matrix[i]:
            out.append(j*j)
        final.append(out[:])
        out.clear()
        i += 1
    return final
