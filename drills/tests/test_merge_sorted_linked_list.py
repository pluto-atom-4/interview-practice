"""
FUNCTION mergeLists(head1, head2):
    // Create a dummy node to act as the starting point
    dummy = NEW SinglyLinkedListNode(0)
    current = dummy

    // Iterate while both lists have nodes remaining
    WHILE head1 IS NOT EMPTY AND head2 IS NOT EMPTY:
        IF head1.data <= head2.data:
            // Attach head1 to the merged list and advance head1
            current.next = head1
            head1 = head1.next
        ELSE:
            // Attach head2 to the merged list and advance head2
            current.next = head2
            head2 = head2.next

        // Move the pointer in the merged list forward
        current = current.next

    // If one list is longer than the other, attach the remainder
    IF head1 IS NOT EMPTY:
        current.next = head1
    ELSE IF head2 IS NOT EMPTY:
        current.next = head2

    // The actual merged list starts after the dummy node
    RETURN dummy.next

"""

import pytest

from drills.merge_sorted_linked_list import mergeLists
from drills.singly_linked_list import SinglyLinkedList, SinglyLinkedListNode


@pytest.mark.parametrize(
    "list1, list2, expected",
    [
        # Basic case: two non-empty lists
        ([1, 3, 5], [2, 4, 6], [1, 2, 3, 4, 5, 6]),
        # One list is empty
        ([], [1, 2, 3], [1, 2, 3]),
        ([1, 2, 3], [], [1, 2, 3]),
        # Both lists are empty
        ([], [], []),
        # Lists with duplicate values
        ([1, 3, 5], [1, 4, 5], [1, 1, 3, 4, 5, 5]),
        # Lists of different lengths
        ([1, 2], [3, 4, 5, 6], [1, 2, 3, 4, 5, 6]),
        ([1, 2, 3, 4], [5], [1, 2, 3, 4, 5]),
    ]
)

def test_mergeLists(list1, list2, expected):
    # Helper function to build a linked list from a list of values
    def build_linked_list(values):
        linked_list = SinglyLinkedList()
        for value in values:
            linked_list.insert_node(value)
        return linked_list.head

    head1 = build_linked_list(list1)
    head2 = build_linked_list(list2)

    merged_head = mergeLists(head1, head2)

    # Convert the merged linked list back to a Python list for easy comparison
    result = []
    current = merged_head
    while current is not None:
        result.append(current.data)
        current = current.next

    assert result == expected