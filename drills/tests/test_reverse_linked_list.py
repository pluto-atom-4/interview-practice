"""
FUNCTION reverse_linked_list(head):
    // Initialize pointers
    prev = NULL
    current = head

    WHILE current is NOT NULL:
        // 1. Save the next node before we break the link
        next_node = current.next

        // 2. Reverse the actual link
        current.next = prev

        // 3. Move pointers forward for the next iteration
        prev = current
        current = next_node

    // prev is the new head of the reversed list
    RETURN prev
"""

import pytest

from drills.reverse_linked_list import (
    build_linked_list,
    linked_list_to_list,
    reverse_linked_list,
)


@pytest.mark.parametrize(
    "values, expected",
    [
        ([1, 2, 3], [3, 2, 1]),
        ([10, 20], [20, 10]),
        ([42], [42]),
        ([], []),
        ([5, 5, 5], [5, 5, 5]),
    ],
)
def test_reverse_linked_list(values, expected):
    head = build_linked_list(values)
    reversed_head = reverse_linked_list(head)
    assert linked_list_to_list(reversed_head) == expected


def test_reverse_twice_returns_original():
    values = [1, 2, 3, 4]
    head = build_linked_list(values)
    reversed_once = reverse_linked_list(head)
    reversed_twice = reverse_linked_list(reversed_once)
    assert linked_list_to_list(reversed_twice) == values
