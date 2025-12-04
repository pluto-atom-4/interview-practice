import pytest

from leetcode.two_sum_naive import two_sum_naive


@pytest.mark.parametrize("nums, target, expected", [
    ([2,7,11,15], 9, [0,1]),
    ([3,2,4], 6, [1,2]),
    ([3,3], 6, [0,1]),
])
def test_two_sum_naive_examples(nums, target, expected):
    result = two_sum_naive(nums, target)
    assert set(result) == set(expected)
