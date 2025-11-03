"""
N-Queens Problem Solver Algorithm Explained Step-by-Step
--------------------------------------------------------
The N-Queens problem is a classic constraint satisfaction problem that demonstrates backtracking algorithms.
The goal is to place N queens on an N×N chessboard such that no two queens can attack each other. Queens can
attack horizontally, vertically, and diagonally. This problem showcases backtracking for systematic search,
constraint checking, and is fundamental for understanding combinatorial optimization and puzzle-solving algorithms.

Here is how the process works:

1. **Initialize Board**: Start with an empty N×N chessboard and place queens row by row.
   - Use array representation where board[i] = j means queen in row i is at column j
   - Initialize board with -1 values indicating no queen placed yet
   - Begin placement from row 0 and proceed systematically

2. **Row-by-Row Placement**: Place one queen per row to automatically avoid row conflicts.
   - Process rows sequentially from 0 to N-1
   - For each row, try placing queen in each column (0 to N-1)
   - Row-wise approach eliminates need to check row conflicts explicitly

3. **Safety Check**: Validate that placing a queen doesn't conflict with existing queens.
   - Column conflict: Check if any previous queen is in the same column
   - Diagonal conflict: Check if any previous queen is on the same diagonal
   - Use mathematical relationship: abs(c1 - c2) == abs(r1 - r2) for diagonal check
   - Only check previous rows since current row is the first placement in that row

4. **Place Queen**: If position is safe, place queen and move to next row.
   - Update board[row] = col to record queen position
   - Make recursive call to place queen in next row (row + 1)
   - Continue building solution incrementally through recursion

5. **Backtrack on Failure**: If no valid position exists in current row, backtrack.
   - Reset current position to -1 (remove queen)
   - Return to previous row to try next column position
   - This systematic undoing explores all possible configurations
   - Ensures complete search space is covered

6. **Solution Found**: When all N queens are placed successfully, record solution.
   - Base case: row == N means all queens placed without conflicts
   - Add current board configuration to solutions list
   - Continue search to find all possible solutions (if multiple solutions exist)

Example: 4-Queens problem on 4×4 board
- Process: Try queen at (0,0), check conflicts, place if safe, recurse to row 1
- Backtrack: If no valid position in row, remove previous queen and try next column
- Result: Valid configurations like [(1,3), (3,0), (0,2), (2,1)]

Time Complexity: O(N!) in worst case, but pruning reduces actual runtime significantly
Space Complexity: O(N) for recursion stack and board representation
Optimization: Constraint checking eliminates many invalid paths early

Why this approach:
- Backtracking systematically explores all possibilities while pruning invalid paths early
- Row-by-row placement reduces the problem complexity by eliminating row conflicts
- Constraint checking at each step prevents exploring obviously invalid solutions
- The recursive structure naturally handles the complex decision tree of valid placements

This algorithm demonstrates backtracking for constraint satisfaction problems and is essential
for understanding systematic search, pruning strategies, and combinatorial problem-solving techniques.
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
