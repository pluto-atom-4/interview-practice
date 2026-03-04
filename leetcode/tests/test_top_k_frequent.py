
import pytest

from leetcode.top_k_frequent import tok_k_frequent

def sort_list(lst):
    return sorted(lst)

@pytest.mark.parametrize(
    "nums, k, expected",
    [
        ([1, 1, 1, 2, 2, 3], 2, [1, 2]),
        ([1], 1, [1]),
        ([4, 4, 4, 6, 6, 7], 1, [4]),
        ([5, 5, 5, 5, 6, 6, 7, 7, 7], 2, [5, 7]),
    ]
)
def test_top_k_frequent(nums, k, expected):
    result = tok_k_frequent(nums, k)
    assert sort_list(result) == sort_list(expected)