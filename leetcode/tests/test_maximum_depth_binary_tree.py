import pytest

from leetcode.maximum_depth_binary_tree import TreeNode, maxDepth


def test_empty_tree():
    assert maxDepth(None) == 0


def test_single_node():
    root = TreeNode(1)
    assert maxDepth(root) == 1


def test_balanced_tree():
    #       1
    #     /   \
    #    2     3
    #   / \
    #  4   5
    root = TreeNode(
        1,
        TreeNode(2, TreeNode(4), TreeNode(5)),
        TreeNode(3)
    )
    assert maxDepth(root) == 3


def test_unbalanced_tree():
    # 1
    #  \
    #   2
    #    \
    #     3
    root = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
    assert maxDepth(root) == 3
