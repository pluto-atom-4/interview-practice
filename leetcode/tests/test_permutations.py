from __future__ import annotations

import pytest

from leetcode.permutations import permute


def sort_permutations(perms):
    """Sort permutations for order‑independent comparison."""
    return sorted([tuple(p) for p in perms])


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1], [[1]]),
        ([1, 2], [[1, 2], [2, 1]]),
        (
            [1, 2, 3],
            [
                [1, 2, 3],
                [1, 3, 2],
                [2, 1, 3],
                [2, 3, 1],
                [3, 1, 2],
                [3, 2, 1],
            ],
        ),
    ],
)
def test_permute(nums, expected):
    result = permute(nums)
    assert sort_permutations(result) == sort_permutations(expected)
