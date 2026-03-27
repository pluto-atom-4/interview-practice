"""
## Problem Statement

Place N queens on an N×N chessboard such that no two queens threaten each other. 
Queens can attack horizontally, vertically, and diagonally. Return all distinct 
valid solutions as a list of board configurations. This is a classic constraint 
satisfaction problem that tests backtracking proficiency and constraint tracking.

## Whiteboard Coding Challenge Notes

* For this problem, I'm using backtracking with constraint sets:

* **Ultra-Minimal One-Liner**:
  - Use backtracking to explore placements row-by-row, tracking occupied columns and 
    diagonals with sets for O(1) constraint checks, achieving O(N!) time.

* **Complexity Analysis**:
  - **Time Complexity:** O(N!) - In the worst case, we explore all possible placements. 
    For each row, we have N choices initially, then N-1, N-2, etc. Set operations 
    (add/remove/lookup) are O(1).
  - **Space Complexity:** O(N²) - The board stores N² cells; the recursion depth is O(N); 
    the three constraint sets store at most O(N) entries each.

## Algorithm Explanation

Backtracking allows us to incrementally build solutions and prune branches that violate 
constraints. By tracking which columns and diagonals are occupied, we avoid expensive 
board scans and make conflict detection O(1).

* Key Concepts:

  - **Row-by-Row Placement Strategy: Why/How?**
    Queens must be placed exactly once per row. By fixing one queen per row and 
    recursing, we enforce the row constraint automatically and reduce the search space 
    from N² cells to N positions per row.

  - **Diagonal Constraint Encoding: Why/How?**
    Two cells (r1, c1) and (r2, c2) share a positive diagonal if r1 - c1 == r2 - c2, 
    and a negative diagonal if r1 + c1 == r2 + c2. Storing these sums in sets enables 
    O(1) conflict detection instead of scanning the entire board.

  - **Backtracking with State Restoration: Why/How?**
    After recursing with a placement, we immediately undo it (restore board, remove 
    from sets) to explore other branches. This memory-efficient approach allows us to 
    reuse the same data structures and avoid redundant copies.

## Algorithm Logic

1. Initialize an empty board, result list, and three constraint sets (columns, 
   positive diagonals, negative diagonals).

   **Why 2D List?** Direct coordinate indexing `board[r][c]` provides O(1) access with
   no hash overhead, unlike dictionary/hash table alternatives. The structure naturally
   maps to chessboard semantics and stores only the N² cells needed with no metadata
   overhead.

2. Define a recursive backtrack function that accepts the current row index.

3. Base case: If row equals N, convert the current board to the required output
      format: a list of strings where each string represents one row. Use
      `["".join(row) for row in board]` to join each row's characters into a single
      string, then append to results.

      **Why this conversion?** The problem requires output as `List[List[str]]`, not
      `List[List[List[str]]]`. Each row must be a single string (e.g., `"Q.Q."`) rather
      than a list of characters (e.g., `["Q", ".", "Q", "."]`). The `.join()` method
      concatenates characters into a string efficiently.

4. For each column in the current row: check if placement is valid by testing the
   three constraint sets.

5. If valid, place the queen, add constraints to sets, and recurse to the next row.

6. After recursion returns, undo the placement and remove constraints (backtrack).

7. Return the results list containing all valid configurations.

## Summary Variations

* **30-Second Pitch**:
  N-Queens uses backtracking to place queens row-by-row. We maintain three sets 
  tracking occupied columns and diagonals. For each row, we try each column; if 
  constraints allow, we place a queen and recurse. After recursion, we undo the 
  placement to explore alternatives. This gives us all valid solutions without 
  scanning the full board—just O(1) set lookups per attempt.

* **Rapid-Fire Version**:
  - Backtrack row-by-row, trying each column
  - Use sets to track column and diagonal occupancy (O(1) lookup)
  - Place queen → recurse → undo placement (state restoration)
  - Base case: all N queens placed → record solution
  - Time: O(N!), Space: O(N²) for board plus recursion

## Use Cases

N-Queens demonstrates core interview concepts: backtracking for constraint satisfaction, 
set-based optimization for conflict detection, and efficient state management. It appears 
in competitive programming, AI search problems, and real-world scheduling (e.g., job 
scheduling, resource allocation) where conflicts must be avoided.
"""

from typing import List

def solve_n_queens(n: int) -> List[List[str]]:

    results: List[List[str]] = []
    board = [["."] * n for _ in range(n)]

    cols = set()
    pos_diag = set()
    neg_diag = set()

    def backtrack(r: int) -> None:
        if r == n:
            results.append(["".join(row) for row in board])
            return

        for c in range(n):
            if c in cols or (r + c) in pos_diag or (r - c) in neg_diag:
                continue

            board[r][c] = "Q"
            cols.add(c)
            pos_diag.add(r + c)
            neg_diag.add(r - c)

            backtrack(r + 1)

            board[r][c] = "."
            cols.remove(c)
            pos_diag.remove(r + c)
            neg_diag.remove(r - c)

    backtrack(0)
    return results