import pytest

from data_structures.trees.tree import Tree, TreeNode


def build_sample_tree():
    #      A
    #     / \
    #    B   C
    #   / \   \
    #  D   E   F
    root = TreeNode("A")
    b = TreeNode("B")
    c = TreeNode("C")
    d = TreeNode("D")
    e = TreeNode("E")
    f = TreeNode("F")
    root.add_child(b)
    root.add_child(c)
    b.add_child(d)
    b.add_child(e)
    c.add_child(f)
    return Tree(root)

def test_preorder():
    tree = build_sample_tree()
    assert list(tree.preorder()) == ["A", "B", "D", "E", "C", "F"]

def test_postorder():
    tree = build_sample_tree()
    assert list(tree.postorder()) == ["D", "E", "B", "F", "C", "A"]

def test_level_order():
    tree = build_sample_tree()
    assert list(tree.level_order()) == ["A", "B", "C", "D", "E", "F"]

def test_empty_tree():
    tree = Tree()
    assert list(tree.preorder()) == []
    assert list(tree.postorder()) == []
    assert list(tree.level_order()) == []

def test_single_node():
    node = TreeNode(1)
    tree = Tree(node)
    assert list(tree.preorder()) == [1]
    assert list(tree.postorder()) == [1]
    assert list(tree.level_order()) == [1]

