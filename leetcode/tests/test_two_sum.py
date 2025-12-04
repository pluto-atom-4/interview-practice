import pytest

from leetcode.two_sum import two_sum


@pytest.mark.parametrize("nums, target", [
    ([2,7,11,15], 9),   # Example 1
    ([3,2,4], 6),       # Example 2
    ([3,3], 6),         # Example 3
])
def test_two_sum_examples(nums, target):
    result = two_sum(nums, target)
    assert len(result) == 2
    i, j = result[0], result[1]
    assert i != j
    assert 0 <= i < len(nums) and 0 <= j < len(nums)
    assert nums[i] + nums[j] == target

def test_two_sum_additional_cases():
    res = two_sum([1,5,3,7], 8)
    assert len(res) == 2
    i, j = res[0], res[1]
    assert i != j
    assert 0 <= i < 4 and 0 <= j < 4
    assert [1,5,3,7][i] + [1,5,3,7][j] == 8

    res = two_sum([10,20,10,40,50,60,70], 50)
    assert len(res) == 2
    i, j = res[0], res[1]
    assert i != j
    assert 0 <= i < 7 and 0 <= j < 7
    assert [10,20,10,40,50,60,70][i] + [10,20,10,40,50,60,70][j] == 50

def test_two_sum_single_pair():
    result = two_sum([1,2], 3)
    assert len(result) == 2
    i, j = result[0], result[1]
    assert i != j
    assert 0 <= i < 2 and 0 <= j < 2
    assert [1,2][i] + [1,2][j] == 3