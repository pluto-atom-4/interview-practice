import pytest


from leetcode.rotting_oranges import oranges_rotting


@pytest.mark.parametrize(
    "grid, expected",
    [
        ([[2,1,1],[1,1,0],[0,1,1]], 4),
        ([[2,1,1],[0,1,1],[1,0,1]], -1),
        ([[0,2]], 0),
        ([[1]], -1),
        ([[2]], 0),
        ([[1, 2]], 1)
    ]
)
def test_oranges_rotting(grid, expected):
    assert oranges_rotting(grid) == expected