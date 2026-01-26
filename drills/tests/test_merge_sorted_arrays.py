import pytest

from drills.merge_sorted_arrays import merge_sorted_arrays_in_place


@pytest.mark.parametrize(
    "a, b, expected_a, expected_b",
    [
        # Equal length (baseline)
        ([1, 3, 5], [2, 4, 6], [1, 2, 3], [4, 5, 6]),

        # Unequal lengths: short + long
        ([1], [2, 3, 4, 5], [1], [2, 3, 4, 5]),
        ([1, 2], [3, 4, 5, 6], [1, 2], [3, 4, 5, 6]),

        # Unequal lengths: long + short
        ([1, 2, 3, 4, 5], [0], [0, 1, 2, 3, 4], [5]),
        ([10, 20, 30, 40], [5], [5, 10, 20, 30], [40]),

        # One array entirely smaller
        ([1, 2, 3], [10, 20], [1, 2, 3], [10, 20]),
        ([10, 20], [1, 2, 3], [1, 2], [3, 10, 20]),

        # One array fits inside the other
        ([1, 10, 20], [2, 3, 4, 5], [1, 2, 3], [4, 5, 10, 20]),
        ([2, 3, 4, 5], [1, 10, 20], [1, 2, 3, 4], [5, 10, 20]),

        # Unequal lengths with duplicates
        ([1, 2, 2, 2], [2, 2, 3], [1, 2, 2, 2], [2, 2, 3]),
        ([2, 2, 3], [1, 2, 2, 2], [1, 2, 2], [2, 2, 2, 3]),

        # Highly uneven: tiny + large
        ([5], [1, 2, 3, 4, 6, 7, 8], [1], [2, 3, 4, 5, 6, 7, 8]),
        ([1, 2, 3, 4, 6, 7, 8], [5], [1, 2, 3, 4, 5, 6, 7], [8]),

        # Empty + non-empty
        ([], [1, 2, 3], [], [1, 2, 3]),
        ([1, 2, 3], [], [1, 2, 3], []),

        # Both empty
        ([], [], [], []),
    ],
)
def test_merge_sorted_arrays_in_place(a, b, expected_a, expected_b):
    merge_sorted_arrays_in_place(a, b)
    assert a == expected_a
    assert b == expected_b
