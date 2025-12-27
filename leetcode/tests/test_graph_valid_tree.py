import pytest

from leetcode.graph_valid_tree import valid_tree


def test_example_valid_tree():
    n = 5
    edges = [[0,1], [0,2], [0,3], [1,4]]
    assert valid_tree(n, edges) is True


def test_cycle_graph():
    n = 3
    edges = [[0,1], [1,2], [2,0]]
    assert valid_tree(n, edges) is False


def test_disconnected_graph():
    n = 4
    edges = [[0,1], [2,3]]
    assert valid_tree(n, edges) is False


def test_single_node():
    assert valid_tree(1, []) is True


def test_two_nodes_connected():
    assert valid_tree(2, [[0,1]]) is True


def test_two_nodes_not_connected():
    assert valid_tree(2, []) is False
