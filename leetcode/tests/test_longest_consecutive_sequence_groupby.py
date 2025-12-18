import pytest

from leetcode.longest_consecutive_sequence_groupby import longest_consecutive_groupby


@pytest.mark.parametrize("nums, expected", [
    ([100,4,200,1,3,2], 4),
    ([0,3,7,2,5,8,4,6,0,1], 9),
    ([1,0,1,2], 3),
    ([], 0),
    ([1], 1),
])
def test_longest_consecutive_groupby(nums, expected):
    assert longest_consecutive_groupby(nums) == expected
