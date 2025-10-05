import pytest

from utils.helpers import is_sorted


# Example function to test — you can replace this with your own implementation
def bubble_sort(arr):
    """
    Simple bubble sort implementation for testing.
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# ✅ Test cases for bubble_sort
@pytest.mark.parametrize(
    "input_arr,expected",
    [
        ([5, 3, 8, 1], [1, 3, 5, 8]),
        ([1, 2, 3], [1, 2, 3]),
        ([3, 2, 1], [1, 2, 3]),
        ([], []),
        ([7], [7]),
    ],
)
def test_bubble_sort(input_arr, expected):
    assert bubble_sort(input_arr) == expected


# ✅ Test cases for is_sorted
@pytest.mark.parametrize(
    "arr,expected",
    [
        ([1, 2, 3, 4], True),
        ([4, 3, 2, 1], False),
        ([1, 1, 2, 2], True),
        ([1], True),
        ([], True),
    ],
)
def test_is_sorted(arr, expected):
    assert is_sorted(arr) == expected


# 🧪 Placeholder for future array problems
def test_array_problem_placeholder():
    assert True  # Replace with actual tests later
