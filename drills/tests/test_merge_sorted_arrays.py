"""
FUNCTION merge_sorted_arrays_in_place(list_a, list_b):
    n = length of list_a
    m = length of list_b
    total_size = n + m

    // Helper to treat list_a and list_b as one contiguous array
    FUNCTION get_value(index):
        IF index < n: RETURN list_a[index]
        ELSE: RETURN list_b[index - n]

    FUNCTION set_value(index, val):
        IF index < n: list_a[index] = val
        ELSE: list_b[index - n] = val

    // Initialize gap
    gap = total_size

    WHILE gap > 1:
        gap = (gap + 1) // 2  // Take the ceiling of gap / 2

        FOR i FROM 0 TO (total_size - gap - 1):
            j = i + gap

            IF get_value(i) > get_value(j):
                temp = get_value(i)
                set_value(i, get_value(j))
                set_value(j, temp)
"""

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
