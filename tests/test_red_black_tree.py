import pytest

from data_structures.trees.red_black_tree import RedBlackTree


def inorder(node, nil):
    if node == nil:
        return []
    return inorder(node.left, nil) + [node.key] + inorder(node.right, nil)


def test_insert_and_search():
    tree = RedBlackTree()
    root = None

    for key in [10, 20, 30, 15]:
        root = tree.insert(root, key)

    assert tree.search(root, 15) is True
    assert tree.search(root, 99) is False


def test_inorder_sorted():
    tree = RedBlackTree()
    root = None

    for key in [7, 3, 18, 10, 22, 8, 11, 26]:
        root = tree.insert(root, key)

    assert inorder(tree.root, tree.nil) == sorted([7, 3, 18, 10, 22, 8, 11, 26])


def test_delete():
    tree = RedBlackTree()
    root = None

    for key in [20, 15, 25, 10, 5]:
        root = tree.insert(root, key)

    root = tree.delete(root, 15)
    assert inorder(tree.root, tree.nil) == [5, 10, 20, 25]
