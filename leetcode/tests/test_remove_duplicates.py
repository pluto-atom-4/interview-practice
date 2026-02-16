import pytest

from leetcode.remove_duplicates import remove_duplicates


@pytest.mark.parametrize(
    "nums, expected_k, expected_prefix",
    [
        ([0,0,1,1,1,2,2,3,3,4], 5, [0,1,2,3,4]),
        ([1,1,2], 2, [1,2]),
        ([1,2,3], 3, [1,2,3]),
        ([5,5,5,5], 1, [5]),
        ([], 0, []),
        ([7], 1, [7]),
        ([1,1,1,2,2,3], 3, [1,2,3]),
    ],
)
def test_remove_duplicates(nums, expected_k, expected_prefix):
    k = remove_duplicates(nums)
    assert k == expected_k
    assert nums[:k] == expected_prefix


def test_large_case():
    nums = sorted(list(range(10000)) + list(range(10000)))  # duplicates
    k = remove_duplicates(nums)
    assert k == 10000
    assert nums[:k] == list(range(10000))
