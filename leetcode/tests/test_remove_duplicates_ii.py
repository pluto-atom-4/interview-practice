import pytest
from leetcode.remove_duplicates_ii import remove_duplicates


@pytest.mark.parametrize(
    "nums, expected_k, expected_prefix",
    [
        ([1,1,1,2,2,3], 5, [1,1,2,2,3]),
        ([0,0,1,1,1,1,2,3,3], 7, [0,0,1,1,2,3,3]),
        ([1,1,2], 3, [1,1,2]),
        ([1,2,3], 3, [1,2,3]),
        ([5,5,5,5], 2, [5,5]),
        ([1], 1, [1]),
        ([1,1], 2, [1,1]),
        ([1,1,1], 2, [1,1]),
    ],
)
def test_remove_duplicates(nums, expected_k, expected_prefix):
    k = remove_duplicates(nums)
    assert k == expected_k
    assert nums[:k] == expected_prefix


def test_large_case():
    nums = [i // 3 for i in range(30000)]  # each number appears 3 times
    k = remove_duplicates(nums)
    assert k == 20000  # each unique number appears twice
    assert nums[:k] == [i // 2 for i in range(20000)]
