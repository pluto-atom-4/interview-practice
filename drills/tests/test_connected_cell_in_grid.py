"""
FUNCTION get_region_size(r, c, grid, visited, rows, cols):
    // Boundary check, wall check (0), or already visited check
    IF r < 0 OR r >= rows OR c < 0 OR c >= cols:
        RETURN 0
    IF grid[r][c] EQUALS 0 OR (r, c) IN visited:
        RETURN 0

    // Mark current cell as visited
    ADD (r, c) TO visited
    size = 1

    // 8-way connectivity directions (Horizontal, Vertical, and Diagonal)
    directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]

    // Recursively explore all neighbors and sum their sizes
    FOR EACH (dr, dc) IN directions:
        size = size + get_region_size(r + dr, c + dc, grid, visited, rows, cols)

    RETURN size


FUNCTION maxRegion(grid):
    IF grid IS EMPTY: RETURN 0

    rows = LENGTH(grid)
    cols = LENGTH(grid[0])
    max_size = 0
    visited = NEW SET

    // Iterate through every cell in the grid
    FOR r FROM 0 TO rows - 1:
        FOR c FROM 0 TO cols - 1:
            // If we find an unvisited filled cell, start a new DFS
            IF grid[r][c] EQUALS 1 AND (r, c) NOT IN visited:
                current_size = get_region_size(r, c, grid, visited, rows, cols)

                // Update global maximum
                IF current_size > max_size:
                    max_size = current_size

    RETURN max_size

"""


import pytest

from drills.connected_cell_in_grid import maxRegion


@pytest.mark.parametrize(
    "grid, expected",
    [
        ([[1, 1, 0], [0, 1, 1], [0, 0, 1]], 5),  # Basic case with one large region
        ([[1, 0, 0], [0, 1, 0], [0, 0, 1]], 3),  # Multiple regions connected diagonally
        ([[0, 0, 0], [0, 0, 0], [0, 0, 0]], 0),  # No filled cells
        ([[1, 1, 1], [1, 1, 1], [1, 1, 1]], 9),  # All cells filled
        ([[1]], 1),  # Single cell filled
        ([[0]], 0),  # Single cell empty
        ([[1, 0], [0, 1]], 2),  # Diagonal connection (8-way)
        ([[1, 1, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 1]], 7),  # Mixed connections with diagonals
    ]
)
def test_maxRegion(grid, expected):
    assert maxRegion(grid) == expected