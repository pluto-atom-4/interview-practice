"""
## Problem Statement

Find the size of the largest connected region in a 2D binary grid where cells with value 1
represent land and cells with value 0 represent water. Two cells are considered connected if 
they are adjacent horizontally, vertically, or diagonally (8-way connectivity). This problem 
tests understanding of graph traversal, DFS optimization, and 2D array navigation.

## Whiteboard Coding Challenge Notes

* For this problem, I'm using **Depth-First Search (DFS) with 8-way connectivity**:

This approach is suitable because we need to explore every connected cell exactly once and
find the maximum region size. DFS naturally handles all connectivity directions and efficiently
tracks visited cells to avoid recomputation.

* Key Concepts:

  - **Why use 8-way directions array instead of manual checks?**
Predefining directions as a static array (-1,-1), (-1,0), ..., (1,1) eliminates code duplication
and makes the 8 neighbor checks explicit and maintainable. This approach is cleaner than writing
eight separate if statements and scales well to different connectivity patterns (4-way, 8-way).

  - **Why use a visited set to track explored cells?**
As we recursively explore neighbors, we mark cells as visited to prevent revisiting the same cell
and entering infinite recursion loops. This ensures each cell is processed once, maintaining O(rows × cols)
time complexity and preventing stack overflow on large connected regions.

  - **Why initialize max_size to 0 and update with max()?**
Starting at 0 handles edge cases (empty grid or all zeros). Using max() ensures we capture the largest
region found. This avoids off-by-one errors and handles the case where no regions exist.

* Logic:

1. **Validate input:** Check for empty grid to avoid index errors
2. **Initialize tracking:** Create a visited set and track grid dimensions (rows, cols)
3. **Define DFS helper:** Create get_region_size(r, c) that recursively explores all 8 neighbors
4. **DFS boundary checks:** Return 0 if out of bounds, cell is water (0), or already visited
5. **Mark and explore:** Add current cell to visited, increment size counter, recurse through all 8 directions
6. **Main loop:** Scan entire grid; when finding unvisited land (1), start DFS and track maximum region size
7. **Return result:** Return the maximum region size found

* **30-Second Pitch**:

I'm using DFS with 8-way connectivity to find the largest connected component in a binary grid.
I predefine all 8 neighbor directions in a static array and recursively explore each unvisited land cell,
marking visited cells to avoid reprocessing. By iterating through the grid and starting DFS from each
unvisited land cell, I track the maximum region size encountered.

* **Rapid-Fire Version**:

- Static 8-direction array avoids code duplication and makes neighbor exploration explicit
- Visited set prevents revisiting cells and infinite recursion
- DFS explores all neighbors recursively, naturally handling arbitrary connectivity patterns
- Main loop initiates DFS from each unvisited land cell
- max() tracks the largest region size encountered
- Time: O(rows × cols) — each cell visited once; Space: O(rows × cols) — visited set and recursion stack

* **Ultra-Minimal One-Liner**:

- DFS with 8-way connectivity and visited tracking finds the largest connected land region in O(rows × cols) time.

* **Complexity Analysis**:

- **Time Complexity:** O(rows × cols) — Each cell is visited exactly once during the DFS traversal. The outer
loop iterates through all cells, and each recursive call explores one new cell, ensuring no redundant work.

- **Space Complexity:** O(rows × cols) — Worst case: visited set stores all cells (entirely connected grid),
and recursion stack depth equals the region size (up to rows × cols in a fully connected grid).

* **Use Cases**:

- Finding largest islands in a grid (geography/map applications)
- Connected component analysis in image processing (blob detection, flood fill)
- Network connectivity analysis (finding largest clusters in distributed systems)
- Game pathfinding and region detection (game board analysis, area-of-effect calculations)
"""

from typing import List

# Static 2D directions array for 8-way connectivity (Horizontal, Vertical, and Diagonal)
DIRECTIONS = [
    (-1, -1), (-1, 0), (-1, 1),  # Top-left, Top, Top-right
    (0, -1),           (0, 1),   # Left, Right
    (1, -1),  (1, 0),  (1, 1),   # Bottom-left, Bottom, Bottom-right
]


def maxRegion(grid: List[List[int]]) -> int:
    if not grid or not grid[0]:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    max_size = 0
    visited = set()

    def dfs(r: int, c: int) -> int:
        # Boundary check and check if cell is filled (1) or already visited
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0 or (r, c) in visited:
            return 0

        # Mark cell as visited
        visited.add((r, c))
        size = 1

        # Check all 8 directions using static directions array
        for dr, dc in DIRECTIONS:
            size += dfs(r + dr, c + dc)

        return size

    # Iterate through every cell in the grid
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and (r, c) not in visited:
                # If we find a filled cell, start a DFS to find the total region size
                current_region_size = dfs(r, c)
                max_size = max(max_size, current_region_size)

    return max_size