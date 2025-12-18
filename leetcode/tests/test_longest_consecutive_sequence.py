import pytest

from leetcode.longest_consecutive_sequence import longest_consecutive


@pytest.mark.parametrize("nums, expected", [
    ([100,4,200,1,3,2], 4),          # Example 1
    ([0,3,7,2,5,8,4,6,0,1], 9),      # Example 2
    ([1,0,1,2], 3),                  # Example 3
    ([], 0),                         # Edge case
    ([1], 1),                        # Single element
    ([9,1,4,7,3,-1,0,5,8,-1,6], 7),  # Mixed values
])
def test_longest_consecutive(nums, expected):
    assert longest_consecutive(nums) == expected
