import pytest

from data_structures.trees.array_binary_tree import ArrayBinaryTree


def test_basic_insert_and_access():
    tree = ArrayBinaryTree()
    tree.insert(0, 10)
    tree.insert(1, 20)
    tree.insert(2, 30)

    assert tree[0] == 10
    assert tree[1] == 20
    assert tree[2] == 30


def test_left_and_right_children():
    tree = ArrayBinaryTree([1, 2, 3, 4, 5])

    assert tree.get_left(0) == 2
    assert tree.get_right(0) == 3
    assert tree.get_left(1) == 4
    assert tree.get_right(1) == 5


def test_parent_lookup():
    tree = ArrayBinaryTree([10, 20, 30, 40])

    assert tree.get_parent(1) == 10
    assert tree.get_parent(2) == 10
    assert tree.get_parent(3) == 20


def test_out_of_bounds_children():
    tree = ArrayBinaryTree([1])

    assert tree.get_left(0) is None
    assert tree.get_right(0) is None


def test_dynamic_expansion():
    tree = ArrayBinaryTree()
    tree.insert(5, 99)

    assert len(tree) == 6
    assert tree[5] == 99
    assert tree[0] is None
    assert tree[4] is None
