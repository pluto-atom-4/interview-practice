import pytest

from algorithms.searching import binary_search


@pytest.mark.parametrize(
    "arr,target,expected",
    [
        ([1, 2, 3, 4, 5], 3, 2),
        ([10, 20, 30, 40], 25, -1),
        ([5], 5, 0),
        ([], 1, -1),
    ],
)
def test_binary_search(arr, target, expected):
    assert binary_search(arr, target) == expected
