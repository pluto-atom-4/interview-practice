import pytest

from leetcode.k_closest_points import k_closest


@pytest.mark.parametrize("points, k, expected", [
    ([[1,3],[-2,2]], 1, [[-2,2]]),  # Example 1
    ([[3,3],[5,-1],[-2,4]], 2, [[3,3],[-2,4]]),  # Example 2 (order may vary)
    ([[0,1],[1,0],[2,2]], 2, [[0,1],[1,0]]),  # Two closest
    ([[1,2]], 1, [[1,2]]),  # Single point
    ([], 0, []),  # Empty input
])
def test_k_closest(points, k, expected):
    result = k_closest(points, k)
    # Compare as sets since order is not guaranteed
    assert sorted(result) == sorted(expected)
