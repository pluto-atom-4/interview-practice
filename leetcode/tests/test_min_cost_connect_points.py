import pytest

from leetcode.min_cost_connect_points import min_cost_connect_points


@pytest.mark.parametrize("points, expected", [
    ([[0,0],[2,2],[3,10],[5,2],[7,0]], 20),   # Example 1
    ([[3,12],[-2,5],[-4,1]], 18),             # Example 2
    ([[0,0],[1,1],[1,0],[-1,1]], 4),          # Example 3
    ([[0,0]], 0),                             # Single point
    ([[0,0],[1,0]], 1),                       # Two points
])
def test_min_cost_connect_points(points, expected):
    assert min_cost_connect_points(points) == expected
