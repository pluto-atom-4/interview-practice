import pytest

from leetcode.spiral_matrix import spiral_order


@pytest.mark.parametrize("matrix, expected", [
    ([[1,2,3],[4,5,6],[7,8,9]], [1,2,3,6,9,8,7,4,5]),  # Example 1
    ([[1,2,3,4],[5,6,7,8],[9,10,11,12]], [1,2,3,4,8,12,11,10,9,5,6,7]),  # Example 2
    ([[1]], [1]),  # Single element
    ([[1,2],[3,4]], [1,2,4,3]),  # 2x2 matrix
    ([[1],[2],[3],[4]], [1,2,3,4]),  # Single column
    ([[1,2,3,4]], [1,2,3,4]),  # Single row
    ([], []),  # Empty matrix
])
def test_spiral_order(matrix, expected):
    assert spiral_order(matrix) == expected
