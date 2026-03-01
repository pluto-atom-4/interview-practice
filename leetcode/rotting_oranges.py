"""
## Problem Statement

Given a 2D grid where cells contain fresh oranges (1), rotten oranges (2), or empty cells (0), 
determine the minimum number of minutes for all fresh oranges to rot via adjacent rotten oranges. 
Return -1 if it's impossible to rot all fresh oranges. This tests multi-source BFS and grid traversal patterns.

## Whiteboard Coding Challenge Notes

* For this problem, I'm using **Multi-Source BFS (Breadth-First Search)**:

The key insight is treating all initially rotten oranges as starting points for a simultaneous spread,
making this naturally a multi-source BFS problem rather than standard single-source BFS. Each minute,
the rot spreads to adjacent fresh cells in parallel.

* Key Concepts:

  - Why Multi-Source BFS instead of DFS?
  
    Multi-source BFS ensures we explore all cells at distance d before distance d+1, which naturally
    gives us the minimum time. Each rotten orange acts as a source spreading simultaneously. DFS would
    require explicit time tracking at each level; BFS gives us level-order traversal "for free" with
    the queue structure. This also prevents overcounting—rotten oranges don't re-rot already rotten cells.

  - Why store (row, col, time) in the queue?
  
    Tracking time in the queue tuple itself means we don't need a separate visited time map. The time
    value represents the exact minute when that orange became rotten. When spreading to neighbors,
    the new time is current_time + 1. The final answer is the maximum time seen across all rotten oranges.

  - Why count fresh oranges and return -1 on mismatch?
  
    Decrementing the fresh count as we rot oranges gives us a quick way to check if all fresh oranges
    were successfully converted. If fresh > 0 after BFS ends, some oranges couldn't reach a rotten source,
    making rotting impossible. This is more efficient than recounting the grid at the end.

* Logic:

1. **Initialization:** Count all rotten oranges (adding each to queue with time 0) and fresh orange count
2. **Edge case:** If no fresh oranges exist, return 0 (nothing to rot)
3. **BFS spread:** Process each rotten orange, checking all 4 adjacent cells for fresh oranges
4. **Rotation:** When a fresh orange at a neighbor is found, mark it as rotten (value 2), decrement fresh count, and queue it with time + 1
5. **Termination:** BFS ends when queue is empty; return max time if all fresh oranges are rotten, else -1

* **30-Second Pitch**:

We treat all initially rotten oranges as simultaneous sources and perform multi-source BFS to spread the rot. 
We store the time when each orange becomes rotten directly in the queue tuple. As we spread to adjacent cells,
we decrement a fresh orange counter and update each newly rotten orange with the next minute value. The maximum
minute tracked is our answer, unless some fresh oranges couldn't be reached—then we return -1.

* **Rapid-Fire Version**:

- Multi-source BFS: start with all rotten oranges in queue simultaneously
- Store (row, col, time) tuples to track when each orange rots
- Spread to 4 adjacent cells (up, down, left, right) each iteration
- Decrement fresh count and update grid as oranges rot
- Answer is max time if fresh == 0, else -1 (unreachable oranges)

* **Ultra-Minimal One-Liner**:

Multi-source BFS from all initially rotten oranges, tracking time in queue tuples and returning max time when all fresh oranges are processed or -1 if any remain unreachable.

* **Complexity Analysis**:

- **Time Complexity:** O(rows × cols) - Each cell is visited at most once (when becoming rotten) and processed once in the queue
- **Space Complexity:** O(rows × cols) - Queue can contain all cells in worst case (all rotten at once or single isolated fresh orange)

* **Use Cases**:

Classic multi-source BFS pattern for "spread from multiple starting points" problems: disease transmission in epidemiology,
infection spread in networks, fire propagation in grids, or finding minimum time to reach all targets from multiple sources.
"""

from collections import deque
from typing import List


def oranges_rotting(grid: List[List[int]]) -> int:
    rows = len(grid)
    cols = len(grid[0])

    que = deque()
    fresh = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                que.append((r,c,0))
            elif grid[r][c] == 1:
                fresh += 1

    if fresh == 0:
        return 0

    minutes = 0
    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    while que:
        r, c, minute = que.popleft()
        minutes = max(minutes, minute)

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if (
                0 <=nr < rows
                and 0 <= nc < cols
                and grid[nr][nc] == 1
            ):
                grid[nr][nc] = 2
                fresh -= 1
                que.append((nr, nc, minutes + 1))

    return minutes if fresh == 0 else -1