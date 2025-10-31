"""
N-Queens Problem Solver
---
- Goal: Place N queens on an N×N chessboard so that no two queens attack each other.
- Constraints: No two queens can share the same row, column, or diagonal.

- Use backtracking to explore valid queen placements row by row.
- Track column and diagonal conflicts to prune invalid paths.
- Return all valid board configurations.
"""


def solve_n_queens(n):
    def is_safe(row, col, board):
        for r in range(row):
            c = board[r]
            if c == col or abs(c - col) == abs(r - row):
                return False
        return True

    def backtrack(row, board, solutions):
        if row == n:
            solutions.append(board[:])
            return
        for col in range(n):
            if is_safe(row, col, board):
                board[row] = col
                backtrack(row + 1, board, solutions)
                board[row] = -1  # backtrack

    solutions = []
    board = [-1] * n
    backtrack(0, board, solutions)
    return solutions


def format_solution(board):
    n = len(board)
    return [
        "".join("Q" if col == board[row] else "." for col in range(n))
        for row in range(n)
    ]
