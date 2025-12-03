import pytest

from leetcode.permutations_ii import permute_unique


@pytest.mark.parametrize("nums, expected", [
    ([1,1,2], [[1,1,2],[1,2,1],[2,1,1]]),  # Example 1
    ([1,2,3], [
        [1,2,3],[1,3,2],
        [2,1,3],[2,3,1],
        [3,1,2],[3,2,1]
    ]),  # Example 2
])
def test_permute_unique(nums, expected):
    result = permute_unique(nums)
    # Compare as sets of tuples since order may vary
    assert set(map(tuple, result)) == set(map(tuple, expected))

def test_empty_list():
    assert permute_unique([]) == [[]]

def test_single_element():
    assert permute_unique([1]) == [[1]]

def test_duplicates():
    result = permute_unique([2,2,1])
    expected = [[1,2,2],[2,1,2],[2,2,1]]
    assert set(map(tuple, result)) == set(map(tuple, expected))
