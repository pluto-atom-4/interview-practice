import pytest

from data_structures.graphs.graph import Graph


def test_add_edge_undirected():
    g = Graph(directed=False)
    g.add_edge("A", "B")
    g.add_edge("A", "C")
    assert set(g.adj_list["A"]) == {"B", "C"}
    assert "A" in g.adj_list["B"]
    assert "A" in g.adj_list["C"]


def test_add_edge_directed():
    g = Graph(directed=True)
    g.add_edge("A", "B")
    g.add_edge("A", "C")
    assert set(g.adj_list["A"]) == {"B", "C"}
    assert "A" not in g.adj_list["B"]
    assert "A" not in g.adj_list["C"]


def test_dfs_traversal(capsys):
    g = Graph()
    g.add_edge("A", "B")
    g.add_edge("A", "C")
    g.add_edge("B", "D")
    g.dfs("A")
    captured = capsys.readouterr()
    output = captured.out.strip().split()
    assert set(output) == {"A", "B", "D", "C"}


def test_bfs_traversal(capsys):
    g = Graph()
    g.add_edge("A", "B")
    g.add_edge("A", "C")
    g.add_edge("B", "D")
    g.bfs("A")
    captured = capsys.readouterr()
    output = captured.out.strip().split()
    assert output[0] == "A"
    assert "B" in output and "C" in output and "D" in output
