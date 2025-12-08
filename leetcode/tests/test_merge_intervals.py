import pytest

from leetcode.merge_intervals import merge


@pytest.mark.parametrize("intervals, expected", [
    ([[1,3],[2,6],[8,10],[15,18]], [[1,6],[8,10],[15,18]]),  # Example 1
    ([[1,4],[4,5]], [[1,5]]),                                # Example 2
    ([[4,7],[1,4]], [[1,7]]),                                # Example 3
    ([], []),                                                # Empty input
    ([[1,2]], [[1,2]]),                                      # Single interval
    ([[1,4],[5,6]], [[1,4],[5,6]]),                          # Non-overlapping
    ([[1,10],[2,3],[4,8]], [[1,10]]),                        # Nested intervals
])
def test_merge(intervals, expected):
    assert merge(intervals) == expected
