from __future__ import annotations

from collections import deque
from typing import Deque, List, Tuple

"""
## Problem Statement

Count the number of connected components ("islands") in a 2D grid where 1 represents land and 0 represents 
water. Islands are connected 4-directionally (up, down, left, right). This tests understanding of graph 
traversal, connected components, and handling 2D grid problems.

## Whiteboard Coding Challenge Notes

* For this problem, I'm using **Breadth-First Search (BFS) with a Visited Matrix**:

BFS systematically explores each connected component without recursion, avoiding potential stack overflow 
on large grids. A visited matrix ensures we don't reprocess cells, and exploring all 4 directions from each 
cell captures the complete connected component before counting it as one island.

* Key Concepts:

  - Why BFS over DFS for 2D grid traversal?
BFS is iterative (using a queue) rather than recursive, preventing stack overflow on very large grids. 
It explores level-by-level, naturally discovering all connected land cells before finishing an island.

  - Why maintain a visited matrix separate from the grid?
Modifying the original grid (marking visited cells with 0) may not be acceptable depending on problem 
constraints. A separate visited matrix preserves the input and provides clearer intent—explicitly tracking 
which cells we've processed. This is a best practice for interview problems.

  - Why check bounds and visited status before adding to queue?
Prevents duplicate processing and out-of-bounds errors. Marking as visited immediately when enqueueing 
(not when de-queuing) avoids adding duplicate entries to the queue, keeping its size manageable.

* Logic:

1. Create a visited matrix of same dimensions as grid, initialized to False
2. Iterate through every cell in the grid
3. When finding an unvisited land cell (value 1), initiate BFS from that cell
4. In BFS: explore all 4 neighbors, marking unvisited land neighbors as visited and enqueueing them
   - **Compute neighbor coordinates (nr, nc):**
     - `nr = r + dr` and `nc = c + dc` transform direction offsets into actual grid positions
     - Offsets `(1,0), (-1,0), (0,1), (0,-1)` represent down, up, right, left
     - Computing new coordinates allows systematic exploration of all adjacent cells
   - **Validate neighbor before enqueueing:**
     - `0 <= nr < rows and 0 <= nc < cols`: Ensure neighbor is within grid bounds (prevents IndexError)
     - `not visited[nr][nc]`: Skip already-visited cells to avoid duplicate processing and infinite loops
     - `grid[nr][nc] == 1`: Only enqueue land cells; water cells (0) don't extend the island
     - **Combined effect:** Only valid, unprocessed land neighbors are added to queue for exploration
5. After BFS completes, increment island counter and continue scanning
6. Return total island count

* **30-Second Pitch**:

I'm using BFS with a separate visited matrix. When I find an unvisited land cell, I explore all connected 
land cells (4-directionally adjacent) using a queue, marking them as visited. Once BFS finishes exploring 
a complete connected component, I count it as one island. This approach is iterative, avoiding stack issues.

* **Rapid-Fire Version**:

- Use visited matrix to track processed cells
- BFS explores all 4-directional neighbors
- Mark visited when enqueueing (not dequeuing) to prevent duplicates
- Each BFS completion = one island
- Iterate through grid to find all starting points

* **Ultra-Minimal One-Liner**:

- BFS-based connected component counter using a visited matrix for 4-directional connectivity in 2D grids.

* **Complexity Analysis**:

- **Time Complexity:** O(rows × cols) — each cell visited at most once during BFS across all islands
- **Space Complexity:** O(rows × cols) — visited matrix + queue in worst case (all land forms one island)

* **Use Cases**:

- Geographic systems counting landmasses
- Network analysis identifying isolated subnets
- Game development: counting connected game regions
"""

def count_islands(grid: List[List[int]]) -> int:
    """
    Count the number of connected components ("islands") in a 2D grid.

    A cell with value 1 is land; 0 is water.
    Connectivity is 4-directional (up, down, left, right).

    Uses BFS for traversal.

    Ex  
        (
            [
                [1, 1, 0, 0],
                [1, 0, 0, 1],
                [0, 0, 1, 1],
                [0, 0, 0, 0],
            ],
            2,
        ),  # Island 1: (0,0)-(0,1)-(1,0); Island 2: (1,3)-(2,3)-(2,2)
    """
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]

    def bfs(start_r: int, start_c: int) -> None:
        queue: Deque[Tuple[int, int]] = deque()
        queue.append((start_r, start_c))
        visited[start_r][start_c] = True

        while queue:
            r, c = queue.popleft()
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if (
                    0 <= nr < rows
                    and 0 <= nc < cols
                    and not visited[nr][nc]
                    and grid[nr][nc] == 1
                ):
                    visited[nr][nc] = True
                    queue.append((nr, nc))

    islands = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and not visited[r][c]:
                bfs(r, c)
                islands += 1

    return islands
