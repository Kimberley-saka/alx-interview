#!/usr/bin/python3
"""
roate 2-d matrix
"""

def rotate_2d_matrix(matrix):
    """
    rotate 2-d matrix 90 degrees clockwise
    """
    size = len(matrix)
    
    # Transpose the matrix
    for i in range(size):
        for j in range(i, size):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Reverse each row to rotate clockwise
    for i in range(size):
        matrix[i].reverse()
