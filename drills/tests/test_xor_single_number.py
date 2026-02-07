"""
FUNCTION xor_single_number(nums):
    // Initialize result with the identity element for XOR
    result = 0

    // XOR every number in the list
    FOR each num in nums:
        result = result XOR num

    // The final value of result is the unique number
    RETURN result
"""

import pytest

from drills.xor_single_number import xor_single_number


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
def test_xor_single_number(nums, expected):
    assert xor_single_number(nums) == expected


def test_large_case():
    nums = list(range(1, 50000))
    nums += list(range(1, 50000))
    nums.append(777777)  # unique
    assert xor_single_number(nums) == 777777
