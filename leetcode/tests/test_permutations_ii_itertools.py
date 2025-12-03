import pytest

from leetcode.permutations_ii_itertools import permute_unique_itertools


@pytest.mark.parametrize("nums, expected", [
    ([1,1,2], [[1,1,2],[1,2,1],[2,1,1]]),
    ([1,2,3], [
        [1,2,3],[1,3,2],
        [2,1,3],[2,3,1],
        [3,1,2],[3,2,1]
    ]),
])
def test_permute_unique_itertools(nums, expected):
    result = permute_unique_itertools(nums)
    assert set(map(tuple, result)) == set(map(tuple, expected))
