"""
FUNCTION count_islands(grid):
    IF grid is empty OR grid[0] is empty: RETURN 0

    num_rows = length of grid
    num_cols = length of grid[0]
    INITIALIZE visited as a 2D boolean array of (num_rows x num_cols) set to False
    islands_count = 0

    // Helper function to traverse and mark a single island
    FUNCTION bfs(start_row, start_col):
        INITIALIZE queue with [(start_row, start_col)]
        SET visited[start_row][start_col] = True

        WHILE queue is not empty:
            (r, c) = REMOVE from front of queue

            // Check 4-directional neighbors: down, up, right, left
            FOR EACH (dr, dc) IN [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr = r + dr
                nc = c + dc

                // Ensure neighbor is within bounds, not visited, and is land
                IF 0 <= nr < num_rows AND 0 <= nc < num_cols:
                    IF visited[nr][nc] is False AND grid[nr][nc] == 1:
                        SET visited[nr][nc] = True
                        ADD (nr, nc) TO end of queue

    // Main loop to scan the entire grid
    FOR r FROM 0 TO num_rows - 1:
        FOR c FROM 0 TO num_cols - 1:
            // If we find unvisited land, it's a new island
            IF grid[r][c] == 1 AND visited[r][c] is False:
                bfs(r, c)
                islands_count = islands_count + 1

    RETURN islands_count

COUNT ISLANDS - SIMPLIFIED FLOWCHART

                          START
                            │
                            ▼
                  ┌───────────────────┐
                  │ Grid empty?       │─ YES ─► RETURN 0
                  └─────────┬─────────┘
                           NO
                            │
                            ▼
                    Initialize visited[][]
                    islands = 0
                            │
                            ▼
                  ┌──────────────────────┐
                  │ FOR each cell (r,c)  │
                  │ in grid              │
                  └────────┬─────────────┘
                           │
                           ▼
                  ┌──────────────────────┐
                  │ Is cell land (1) AND │
                  │ unvisited?           │─ No ─► Next cell
                  └─────────┬────────────┘
                           YES
                            │
                            ▼
                      BFS(r, c)
                            │
                            ▼
                      Mark visited & explore all 4-neighbors
                            │
                            ▼
                      islands += 1
                            │
                            ▼
                    ┌─────────────────┐
                    │ All cells done? │─ YES ─► RETURN islands
                    └───────┬─────────┘
                           NO
                            │ Return
                            ▼ to loop
                        (next cell)
"""

import pytest

from drills.count_islands import count_islands


@pytest.mark.parametrize(
    "grid, expected",
    [
        (
            [
                [1, 1, 0, 0],
                [1, 0, 0, 1],
                [0, 0, 1, 1],
                [0, 0, 0, 0],
            ],
            2,
        ),  # Island 1: (0,0)-(0,1)-(1,0); Island 2: (1,3)-(2,3)-(2,2)
        (
            [
                [1, 1, 1],
                [1, 1, 1],
            ],
            1,
        ),
        (
            [
                [1, 0, 1],
                [0, 1, 0],
                [1, 0, 1],
            ],
            5,
        ),
        (
            [
                [0, 0, 0],
                [0, 0, 0],
            ],
            0,
        ),
        (
            [],
            0,
        ),
        (
            [[]],
            0,
        ),
    ],
)
def test_count_islands(grid, expected):
    assert count_islands(grid) == expected
