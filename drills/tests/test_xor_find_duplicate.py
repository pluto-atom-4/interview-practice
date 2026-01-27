import pytest

from drills.xor_find_duplicate import xor_find_duplicate


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 3, 4, 2, 2], 2),
        ([1, 1], 1),
        ([2, 1, 3, 4, 2], 2),
        ([3, 1, 3, 4, 2], 3),
        ([5, 4, 3, 2, 1, 3], 3),
        ([1, 2, 3, 4, 5, 6, 6], 6),
        ([5, 4, 3, 2, 1, 3], 3),
    ],
)
def test_xor_find_duplicate(nums, expected):
    assert xor_find_duplicate(nums) == expected


def test_large_case():
    nums = list(range(1, 10001))
    nums.append(777)  # duplicate
    assert xor_find_duplicate(nums) == 777
