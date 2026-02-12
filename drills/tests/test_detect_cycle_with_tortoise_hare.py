"""
FUNCTION has_cycle(head):
    IF head IS EMPTY:
        RETURN False

    // Initialize two pointers at the start
    // slow moves 1 step, fast moves 2 steps
    slow = head
    fast = head

    // Traverse the list as long as the fast pointer can move two steps
    WHILE fast IS NOT EMPTY AND fast.next IS NOT EMPTY:
        // Move pointers forward
        slow = slow.next
        fast = fast.next.next

        // If pointers meet at the same node, a cycle exists
        IF slow EQUALS fast:
            RETURN True

    // If fast reaches the end of the list, there is no cycle
    RETURN False
"""

import pytest

from drills.detect_cycle_with_tortoise_hare import has_cycle
from drills.singly_linked_list import SinglyLinkedListNode


@pytest.fixture
def cyclic_list():
    # Create a cyclic linked list: 1 -> 2 -> 3 -> 4 -> 2 (cycle back to node with value 2)
    node1 = SinglyLinkedListNode(1)
    node2 = SinglyLinkedListNode(2)
    node3 = SinglyLinkedListNode(3)
    node4 = SinglyLinkedListNode(4)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2  # Creates the cycle

    return node1

@pytest.fixture
def acyclic_list():
    # Create an acyclic linked list: 1 -> 2 -> 3 -> 4 -> None
    node1 = SinglyLinkedListNode(1)
    node2 = SinglyLinkedListNode(2)
    node3 = SinglyLinkedListNode(3)
    node4 = SinglyLinkedListNode(4)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = None  # No cycle

    return node1

def test_has_cycle_with_cycle(cyclic_list):
    assert has_cycle(cyclic_list) == True

def test_has_cycle_without_cycle(acyclic_list):
    assert has_cycle(acyclic_list) == False