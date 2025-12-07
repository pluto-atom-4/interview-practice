"""
Maximum Area of Island (BFS Approach) - Algorithm Explained Step-by-Step
--------------------------------------------------------------------------
The Maximum Area of Island problem using Breadth-First Search (BFS) is an alternative approach to finding
the largest connected component of land cells in a grid. While DFS uses recursion, BFS uses an explicit queue
for iterative traversal. Both approaches have the same time complexity but differ in space usage and implementation.
This version is useful when avoiding deep recursion stacks or demonstrating queue-based graph traversal.

Here is how the process works:

1. **Problem Understanding**: Given a 2D grid with 1s (land) and 0s (water).
   - Find the maximum area of connected land cells (cells connected horizontally/vertically)
   - Connected means adjacent in 4 directions: up, down, left, right (not diagonals)
   - Area is the count of land cells in a connected component

2. **Base Case Handling**: Check for empty or invalid grids.
   - Return 0 if grid is None, empty, or has no columns
   - Prevents errors when traversing non-existent grid cells

3. **BFS Helper Function**: Uses a queue for level-by-level traversal.
   - Initialize queue with starting land cell coordinates
   - Mark the starting cell as visited (set to 0) to prevent revisiting
   - While queue is not empty: dequeue a cell, increment area counter
   - For each of 4 adjacent directions (up, down, left, right):
     - Check if neighbor is within bounds and is land (1)
     - If valid and unvisited, mark as visited and enqueue it
   - Return total area when queue becomes empty (all connected cells visited)

4. **Boundary Checking**: Essential to prevent out-of-bounds access.
   - Check if neighbor position is within grid bounds (0 to rows/cols)
   - Stop expansion if we hit water (0) or boundary
   - Check conditions before adding to queue (prevents invalid additions)

5. **Queue-Based Traversal**: Level-order exploration of connected component.
   - Queue ensures cells are explored in order they're discovered (FIFO)
   - Unlike DFS which goes deep first, BFS explores width-first
   - All neighbors at distance k are visited before neighbors at distance k+1
   - This approach is iterative, avoiding recursion depth limitations

6. **Main Iteration**: Scan entire grid to find all islands.
   - Iterate through every cell in the grid
   - When we find an unvisited land cell (1), start a BFS from there
   - Track the maximum area found across all islands
   - The BFS will visit and mark all connected cells as visited

7. **Return Maximum**: The answer is the largest island area found.
   - After scanning entire grid, return the maximum area encountered
   - This represents the size of the largest connected component of land

Example: grid = [[1,1,0,0,0],[1,1,0,0,0],[0,0,1,0,0],[0,0,0,1,1]]
- First island: top-left with area 4 (2x2 block)
- Second island: middle cell with area 1
- Third island: bottom-right with area 2 (1x2 block)
- Result: 4 (largest island)

Time Complexity: O(m * n) where m = rows, n = columns (visit each cell once)
Space Complexity: O(min(m, n)) for the queue in best case, O(m * n) in worst case
  - Best case: queue contains only a few cells at a time (scattered islands)
  - Worst case: entire grid is one island (queue may contain O(m*n) cells)
  - Better than DFS recursion stack in cases with very large connected components

Advantages of BFS over DFS:
- No risk of stack overflow on deep recursion
- Can be easier to understand for iterative thinkers
- Natural for level-based traversal problems
- Can be optimized with sentinel values to reduce queue operations

Disadvantages:
- Explicit queue requires more code
- Space usage may be higher for sparse graphs
- Less cache-friendly than DFS in some scenarios

This algorithm demonstrates BFS for graph connectivity problems, important for understanding
iterative graph traversal, queue-based algorithms, and alternatives to recursive solutions.
"""

from collections import deque
from typing import List


def max_area_of_island_bfs(grid: List[List[int]]) -> int:
    """
    Return the maximum area of an island in the grid using BFS.
    """
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])

    def bfs(r: int, c: int) -> int:
        queue = deque([(r, c)])
        grid[r][c] = 0  # mark visited
        area = 0
        while queue:
            x, y = queue.popleft()
            area += 1
            for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                    grid[nx][ny] = 0
                    queue.append((nx, ny))
        return area

    max_area = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                max_area = max(max_area, bfs(r, c))

    return max_area
