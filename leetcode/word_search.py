"""
## Problem Statement

Given an m x n board containing characters and a string word, determine if the 
word exists in the board. The word must be formed by cells connected adjacently 
(horizontally or vertically), and each cell can be used at most once.

## Whiteboard Coding Challenge Notes

* For this problem, I'm using **Depth-First Search (DFS) with Backtracking**:

* **Ultra-Minimal One-Liner**:

- Recursively search all adjacent cells using DFS with in-place marking to avoid 
revisiting cells; backtrack by restoring the original character.

* **Complexity Analysis**:

- **Time Complexity:** O(m * n * 4^L) where m, n are board dimensions and L is 
word length. For each starting cell (m * n), DFS explores up to 4 directions 
recursively to depth L.
- **Space Complexity:** O(L) for the recursion stack (maximum depth is word length).

## Algorithm Explanation

DFS with backtracking is ideal here because we need to explore all possible paths 
from each starting cell without reusing cells in a single path. Backtracking (via 
in-place board modification) avoids extra visited sets and allows us to try 
multiple paths.

* Key Concepts:

  - **In-Place Marking Instead of Visited Set**: Why/How?
  Why: Using a separate visited set adds O(m * n) space complexity; marking cells 
  with a placeholder (e.g., "#") avoids extra memory overhead. How: Before 
  exploring neighbors, replace the current cell with a sentinel value. If the path 
  fails, restore the original character during backtracking. This ensures each 
  cell is usable in different path explorations.

  - **Recursive Base Cases**: Why/How?
  Why: Clear termination prevents infinite loops and wasted recursion. How: Return 
  True if we've matched all characters (i == len(word)). Return False if we're 
  out of bounds or the current cell doesn't match word[i]. These checks ensure 
  we only continue valid paths.

  - **Early Termination on Success**: Why/How?
  Why: Once a valid path is found, there's no need to explore further; returning 
  immediately improves performance. How: Each DFS call returns True as soon as a 
  complete match is found, propagating the success back through the call stack.

## Algorithm Logic

1. **Initialization**: Check for empty board; cache board dimensions (rows, cols).
2. **Define DFS Helper**: Create a recursive function that takes current position 
(dr, dc) and word index (i).
3. **Base Case - Match Found**: If i equals word length, return True (entire word 
matched).
4. **Boundary and Character Validation**: Return False if out of bounds or current 
cell doesn't match word[i].
5. **Mark Cell as Visited**: Replace current cell with "#" to prevent revisiting 
in this path.
6. **Explore Neighbors**: Recursively call DFS on all 4 adjacent cells with 
incremented word index.
7. **Backtrack**: If any neighbor leads to a match, restore the cell and return 
True. If no neighbor matches, restore and return False.
8. **Main Search**: Iterate through all board cells as potential starting points.
9. **Return Result**: Return True if any starting cell leads to a complete word 
match.

## Summary Variations

* **30-Second Pitch**:

"I'm using depth-first search with backtracking to find the word. For each cell 
as a starting point, I recursively explore adjacent cells while checking if they 
match the next character in the word. To avoid revisiting cells in the same path, 
I mark visited cells with a placeholder and restore them when backtracking. This 
way, I avoid extra space for a visited set while efficiently pruning invalid 
paths."

* **Rapid-Fire Version**:

- DFS explores all adjacent cells recursively from each starting position
- In-place marking (replacing with "#") tracks visited cells without extra space
- Backtracking restores cells when paths fail, enabling multi-path exploration
- Early termination returns True on first complete word match
- Time complexity is O(m * n * 4^L); space is O(L) for recursion stack

## Use Cases:

Word search is common in word game solvers, spell-checkers, and puzzle games like 
Boggle. The backtracking approach is fundamental for constraint satisfaction 
problems where you need to explore all valid configurations while pruning invalid 
ones early.
"""

from typing import List

DIRECTIONS: tuple[tuple[int, int], ...] = (
    (1,  0), (-1, 0),
    (0, -1), ( 0, 1)
)

def exist(board: List[List[str]], word: str) -> bool:
    if not board or not board[0]:
        return False

    rows, cols = len(board), len(board[0])

    def dfs(dr: int, dc:int, i:int) -> bool:
        if i == len(word):
            return True

        if (
            dr < 0 or dr >= rows or
            dc < 0 or dc >= cols or
            board[dr][dc] != word[i]
        ):
            return False

        temp = board[dr][dc]
        board[dr][dc] = "#"

        for dr_offset, dc_offset in DIRECTIONS:
            if dfs(dr + dr_offset, dc + dc_offset, i + 1):
                board[dr][dc] = temp
                return True

        board[dr][dc] = temp
        return False

    for r in range(rows):
        for c in range(cols):
            if dfs(r, c, 0):
                return True

    return False