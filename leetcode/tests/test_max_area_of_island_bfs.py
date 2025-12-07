import pytest

from leetcode.max_area_of_island_bfs import max_area_of_island_bfs


@pytest.mark.parametrize("grid, expected", [
    (
        [[0,0,1,0,0,0,0,1,0,0,0,0,0],
         [0,0,0,0,0,0,0,1,1,1,0,0,0],
         [0,1,1,0,1,0,0,0,0,0,0,0,0],
         [0,1,0,0,1,1,0,0,1,0,1,0,0],
         [0,1,0,0,1,1,0,0,1,1,1,0,0],
         [0,0,0,0,0,0,0,0,0,0,1,0,0],
         [0,0,0,0,0,0,0,1,1,1,0,0,0],
         [0,0,0,0,0,0,0,1,1,0,0,0,0]],
        6
    ),  # Example 1
    ([[0,0,0,0,0,0,0,0]], 0),  # Example 2
    ([[1]], 1),  # Single cell island
    ([[0]], 0),  # Single cell water
    ([[1,1,0,0],[1,0,0,1],[0,0,1,1]], 3),  # Custom case
])
def test_max_area_of_island_bfs(grid, expected):
    import copy
    assert max_area_of_island_bfs(copy.deepcopy(grid)) == expected
