import pytest

from leetcode.kth_smallest_pair_distance import smallest_distance_pair


@pytest.mark.parametrize("nums, k, expected", [
    ([1,3,1], 1, 0),   # Example 1
    ([1,1,1], 2, 0),   # Example 2
    ([1,6,1], 3, 5),   # Example 3
    ([1,2,3], 2, 1),   # Pairs: (1,2)=1, (2,3)=1, (1,3)=2
    ([9,10,7,10,6,1], 5, 2), # Custom case - sorted [1,6,7,9,10,10]: pairs (10,10)=0, (6,7)=1, (9,10)=1, (9,10)=1, (7,9)=2 -> 5th is 2
])
def test_smallest_distance_pair(nums, k, expected):
    assert smallest_distance_pair(nums, k) == expected

def test_edge_cases():
    assert smallest_distance_pair([1,1], 1) == 0  # Only one pair
    assert smallest_distance_pair([1,100], 1) == 99  # Large distance
