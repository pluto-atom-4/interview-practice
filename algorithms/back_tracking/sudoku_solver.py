"""
Sudoku Solver Overview
Goal: Fill a 9×9 grid so that each row, column, and 3×3 box contains digits 1–9 exactly once.

Approach: Use backtracking to try digits in empty cells, validate constraints, and backtrack when stuck.
"""

def is_valid(board, row, col, num):
    block_row = 3 * (row // 3)
    block_col = 3 * (col // 3)
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
        if board[block_row + i // 3][block_col + i % 3] == num:
            return False
    return True


def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == ".":
                for num in map(str, range(1, 10)):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = "."  # backtrack
                return False
    return True
