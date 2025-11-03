"""
Sudoku Solver Algorithm Explained Step-by-Step
----------------------------------------------
The Sudoku Solver is a classic constraint satisfaction problem that uses backtracking to fill a 9×9 grid
where each row, column, and 3×3 sub-box must contain all digits 1-9 exactly once. This algorithm demonstrates
backtracking for systematic search with constraint checking, making it fundamental for understanding
puzzle-solving algorithms, constraint satisfaction problems, and recursive problem-solving techniques.

Here is how the process works:

1. **Find Empty Cell**: Scan the board row by row to locate the first empty cell (marked with ".").
   - Start from position (0,0) and move systematically across rows
   - When an empty cell is found, attempt to place digits 1-9
   - If no empty cells remain, the puzzle is solved successfully

2. **Try Each Digit**: For each empty cell, attempt to place digits 1 through 9.
   - Iterate through all possible digits systematically
   - Test each digit against Sudoku constraints before placement
   - Only proceed if the digit placement is valid according to rules

3. **Validate Constraints**: Check if placing a digit violates Sudoku rules.
   - Row constraint: Digit must not already exist in the same row
   - Column constraint: Digit must not already exist in the same column
   - 3×3 box constraint: Digit must not exist in the current 3×3 sub-grid
   - All three constraints must be satisfied simultaneously

4. **Place and Recurse**: If a digit is valid, place it and recursively solve the rest.
   - Update the board with the valid digit
   - Make recursive call to solve remaining empty cells
   - If recursive call returns True, solution is found
   - Continue building solution incrementally through recursion

5. **Backtrack on Failure**: If no valid digit works, backtrack to previous state.
   - Reset current cell to empty (".") to undo the placement
   - Return False to indicate this path doesn't lead to solution
   - Algorithm backtracks to previous recursive call to try next option
   - This systematic undoing enables exploration of all possibilities

6. **Solution Complete**: When no empty cells remain, the puzzle is solved.
   - Base case: All cells filled with valid digits
   - Return True to propagate success back through recursive calls
   - Final board state contains the complete Sudoku solution
   - Algorithm terminates with successful solution found

Example: Solving a partially filled 9×9 Sudoku grid
- Process: Find empty cell at (0,0), try digits 1-9, validate constraints
- Valid digit found: Place it, recurse to next empty cell
- Invalid paths: Backtrack and try next digit option
- Result: Complete 9×9 grid with all constraints satisfied

Time Complexity: O(9^(n*n)) in worst case, where n=9 for standard Sudoku
Space Complexity: O(n*n) for the recursion stack in worst case
Optimization: Constraint checking prunes many invalid paths early

Why this approach:
- Backtracking is ideal for constraint satisfaction problems like Sudoku
- The algorithm explores all possibilities systematically while pruning invalid paths early
- Cell-by-cell placement with immediate constraint checking ensures efficiency
- The recursive nature naturally handles the complex decision tree of valid placements

This algorithm demonstrates backtracking for puzzle solving and is essential for understanding
systematic search, constraint satisfaction, and recursive problem-solving strategies.
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
