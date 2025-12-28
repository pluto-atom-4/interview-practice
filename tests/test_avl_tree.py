import pytest

from data_structures.trees.avl_tree import AVLNode, AVLTree


def inorder(root):
    if root is None:
        return []
    return inorder(root.left) + [root.key] + inorder(root.right)


def test_insert_balances_tree():
    tree = AVLTree()
    root = None

    for key in [10, 20, 30]:
        root = tree.insert(root, key)

    assert inorder(root) == [10, 20, 30]
    assert root.key == 20  # rotation happened


def test_delete_node():
    tree = AVLTree()
    root = None

    for key in [20, 10, 30, 25, 40]:
        root = tree.insert(root, key)

    root = tree.delete(root, 30)
    assert inorder(root) == [10, 20, 25, 40]


def test_search():
    tree = AVLTree()
    root = None

    for key in [5, 2, 8, 1, 3]:
        root = tree.insert(root, key)

    assert tree.search(root, 3) is True
    assert tree.search(root, 10) is False


def test_balancing_after_multiple_inserts():
    tree = AVLTree()
    root = None

    for key in [50, 20, 60, 10, 25, 70, 5]:
        root = tree.insert(root, key)

    assert inorder(root) == [5, 10, 20, 25, 50, 60, 70]
    assert abs(tree._balance(root)) <= 1
