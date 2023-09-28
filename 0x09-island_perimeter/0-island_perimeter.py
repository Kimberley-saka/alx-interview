#!/usr/bin/python3
"""
Perimeter of an island
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of an island
    """
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4

                # Check the left and upper neighbor
                if i > 0 and grid[i-1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j-1] == 1:
                    perimeter -= 2

    return perimeter
