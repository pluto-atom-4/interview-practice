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

from drills.binary_search_tree import Node
from drills.lca import lca


@pytest.mark.parametrize(
    "root, v1, v2, expected",
    [
        # Basic case: LCA is the root
        ([5, 3, 7], 3, 7, 5),
        # LCA is a child node
        ([5, 3, 7], 3, 4, 3),
        # LCA is a deeper node
        ([5, 3, 7, 2, 4], 2, 4, 3),
        # One value is the ancestor of the other
        ([5, 3, 7], 3, 2, 3),
        # Both values are the same
        ([5, 3, 7], 3, 3, 3),
        # Values not in the tree
        ([5, 3, 7], 1, 2, None),
        # Empty tree
        ([], 1, 2, None),
        # Skewed tree (all right)
        ([1, None, 2, None, 3], 2, 3  , 2),
        # Skewed tree (all left)
        ([3, 2, 1], 1, 2, 2),
    ]
)

def test_lca(root, v1, v2, expected):
    # Helper function to build a BST from a list
    def insert_into_bst(root, val):
        if root is None:
            return Node(val)
        if val < root.info:
            root.left = insert_into_bst(root.left, val)
        else:
            root.right = insert_into_bst(root.right, val)
        return root

    # Build the BST
    bst_root = None
    for value in root:
        if value is not None:
            bst_root = insert_into_bst(bst_root, value)

    # Call the LCA function and check the result
    result_node = lca(bst_root, v1, v2)
    result_value = result_node.info if result_node else None
    assert result_value == expected