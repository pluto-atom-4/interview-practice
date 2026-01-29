"""
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
