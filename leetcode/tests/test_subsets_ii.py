import pytest

from leetcode.subsets_ii import subsets_with_dup


def normalize(subsets):
    return sorted([tuple(sorted(s)) for s in subsets])

@pytest.mark.parametrize(
    "nums, expected",
    [
        (
            [1, 2, 2],
            [
                [],
                [1],
                [2],
                [1, 2],
                [2, 2],
                [1, 2, 2],
            ],
        ),
        (
            [0],
            [
                [],
                [0],
            ],
        ),
    ],
)
def test_subsets_with_dup(nums, expected):
    result = subsets_with_dup(nums)
    assert normalize(result) == normalize(expected)