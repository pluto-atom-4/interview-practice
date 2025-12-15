import pytest

from leetcode.move_zeroes_reduce import move_zeroes_reduce


@pytest.mark.parametrize("nums, expected", [
    ([0,1,0,3,12], [1,3,12,0,0]),
    ([0], [0]),
    ([1,2,3], [1,2,3]),
    ([0,0,1], [1,0,0]),
    ([4,0,5,0,0,6], [4,5,6,0,0,0]),
])
def test_move_zeroes_reduce(nums, expected):
    move_zeroes_reduce(nums)
    assert nums == expected
