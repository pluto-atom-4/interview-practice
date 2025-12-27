import pytest

from leetcode.maximum_depth_array_binary_tree import max_depth_array_tree


def test_empty_tree():
    assert max_depth_array_tree([]) == 0


def test_single_node():
    assert max_depth_array_tree([1]) == 1


def test_full_tree():
    #       1
    #     /   \
    #    2     3
    #   / \
    #  4   5
    values = [1, 2, 3, 4, 5]
    assert max_depth_array_tree(values) == 3


def test_tree_with_missing_nodes():
    #       1
    #     /   \
    #    2     None
    #   /
    #  4
    values = [1, 2, None, 4]
    assert max_depth_array_tree(values) == 3


def test_unbalanced_right():
    # 1
    #  \
    #   3
    #    \
    #     7
    values = [1, None, 3, None, None, None, 7]
    assert max_depth_array_tree(values) == 3
