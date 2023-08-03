"""
solution to the n-queens problem
"""
import sys


def is_safe(board, row, col):
    """
    Check if there is a queen in the same column
    """
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True


def nqueens(board, row):
    """
    check for stopping condition and backtrack to find a suitable placement
    of queen
    """
    n = len(board)
    if row == n:  # Stopping condition
        print([[r, board[r]] for r in range(n)])
        return

    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            nqueens(board, row + 1)


def main():
    """
    check for input, usage and value type
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * N
    nqueens(board, 0)


if __name__ == "__main__":
    main()
