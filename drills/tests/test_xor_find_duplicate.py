"""
FUNCTION xor_find_duplicate(nums):
    n = length of nums - 1

    xor_all_nums = 0
    xor_1_to_n = 0

    // Step 1: XOR all elements present in the input array
    FOR each num in nums:
        xor_all_nums = xor_all_nums XOR num

    // Step 2: XOR all possible numbers in the range [1, n]
    FOR i FROM 1 TO n:
        xor_1_to_n = xor_1_to_n XOR i

    // Step 3: Combine the results to reveal the duplicate
    // Identical numbers cancel out (a XOR a = 0), leaving only the duplicate
    RETURN xor_all_nums XOR xor_1_to_n

"""

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
