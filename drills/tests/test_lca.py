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