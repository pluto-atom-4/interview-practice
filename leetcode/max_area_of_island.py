"""
Maximum Area of Island (DFS Approach) - Algorithm Explained Step-by-Step
--------------------------------------------------------------------------
The Maximum Area of Island problem is a classic graph/matrix traversal problem that finds the largest
connected component of land cells (represented by 1s) in a grid. Water cells are represented by 0s.
This problem demonstrates depth-first search (DFS) for exploring connected components and is essential
for understanding graph traversal, flood fill algorithms, and spatial connectivity problems.

Here is how the process works:

1. **Problem Understanding**: Given a 2D grid with 1s (land) and 0s (water).
   - Find the maximum area of connected land cells (cells connected horizontally/vertically)
   - Connected means adjacent in 4 directions: up, down, left, right (not diagonals)
   - Area is the count of land cells in a connected component

2. **Base Case Handling**: Check for empty or invalid grids.
   - Return 0 if grid is None, empty, or has no columns
   - Prevents errors when traversing non-existent grid cells

3. **DFS Helper Function**: Recursively explore all connected land cells.
   - Start from an unvisited land cell (value 1)
   - Mark current cell as visited by setting it to 0 (prevents revisiting)
   - Recursively call DFS on all 4 adjacent neighbors (up, down, left, right)
   - Sum the area from all recursive calls
   - Return the total area of this connected component

4. **Boundary Checking**: Essential to prevent out-of-bounds access.
   - Check if current position is within grid bounds (0 to rows/cols)
   - Stop recursion if we hit water (0) or boundary

5. **Main Iteration**: Scan entire grid to find all islands.
   - Iterate through every cell in the grid
   - When we find an unvisited land cell (1), start a DFS from there
   - Track the maximum area found across all islands
   - The DFS will visit and mark all connected cells as visited

6. **Return Maximum**: The answer is the largest island area found.
   - After scanning entire grid, return the maximum area encountered
   - This represents the size of the largest connected component of land

Example: grid = [[1,1,0,0,0],[1,1,0,0,0],[0,0,1,0,0],[0,0,0,1,1]]
- First island: top-left with area 4 (2x2 block)
- Second island: middle cell with area 1
- Third island: bottom-right with area 2 (1x2 block)
- Result: 4 (largest island)

Time Complexity: O(m * n) where m = rows, n = columns (visit each cell once)
Space Complexity: O(m * n) for recursion call stack in worst case (single large island)
  - Maximum recursion depth is m*n in worst case (entire grid is one island)
  - Average case is better, depending on island distribution

This algorithm demonstrates DFS for graph connectivity problems, critical for understanding
connected components, island problems, flood fill algorithms, and spatial data analysis.
"""

from typing import List


def max_area_of_island(grid: List[List[int]]) -> int:
    """
    Return the maximum area of an island in the grid.
    Uses DFS to explore connected components.
    """
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])

    def dfs(r: int, c: int) -> int:
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
            return 0
        grid[r][c] = 0  # mark visited
        area = 1
        area += dfs(r + 1, c)
        area += dfs(r - 1, c)
        area += dfs(r, c + 1)
        area += dfs(r, c - 1)
        return area

    max_area = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                max_area = max(max_area, dfs(r, c))

    return max_area
