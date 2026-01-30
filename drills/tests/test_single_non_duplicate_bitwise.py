import pytest

from drills.single_non_duplicate_bitwise import single_non_duplicate_bitwise


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([2, 2, 1], 1),
        ([4, 1, 2, 1, 2], 4),
        ([99], 99),
        ([7, 3, 7], 3),
        ([10, 10, 20, 20, 30], 30),
        ([42, 42, 42, 42, 99, 99, 100], 100),
    ],
)
def test_single_non_duplicate_bitwise(nums, expected):
    assert single_non_duplicate_bitwise(nums) == expected


def test_large_case():
    nums = list(range(1, 50000))
    nums += list(range(1, 50000))
    nums.append(777777)  # unique
    assert single_non_duplicate_bitwise(nums) == 777777
