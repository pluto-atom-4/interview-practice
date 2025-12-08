import pytest

from leetcode.merge_intervals_naive import merge_naive


@pytest.mark.parametrize("intervals, expected", [
    ([[1,3],[2,6],[8,10],[15,18]], [[1,6],[8,10],[15,18]]),
    ([[1,4],[4,5]], [[1,5]]),
    ([[4,7],[1,4]], [[1,7]]),
    ([], []),
    ([[1,2]], [[1,2]]),
])
def test_merge_naive(intervals, expected):
    result = merge_naive(intervals)
    assert sorted(result) == sorted(expected)
