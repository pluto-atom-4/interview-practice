import pytest

from data_structures.graphs.dependency_graph import DependencyGraph


def test_no_cycle():
    g = DependencyGraph()
    g.add_dependency("A", "B")
    g.add_dependency("B", "C")
    g.add_dependency("C", "D")

    assert g.has_cycle() is False
    assert g.get_cycle_nodes() is None


def test_simple_cycle():
    g = DependencyGraph()
    g.add_dependency("A", "B")
    g.add_dependency("B", "C")
    g.add_dependency("C", "A")

    assert g.has_cycle() is True
    cycle = g.get_cycle_nodes()
    assert set(cycle) == {"A", "B", "C"}


def test_disconnected_graph():
    g = DependencyGraph()
    g.add_dependency("A", "B")
    g.add_dependency("C", "D")

    assert g.has_cycle() is False


def test_cycle_in_subgraph():
    g = DependencyGraph()
    g.add_dependency("A", "B")
    g.add_dependency("B", "C")
    g.add_dependency("X", "Y")
    g.add_dependency("Y", "Z")
    g.add_dependency("Z", "X")  # cycle here

    assert g.has_cycle() is True
    cycle = g.get_cycle_nodes()
    assert set(cycle) == {"X", "Y", "Z"}


def test_add_node_without_dependencies():
    g = DependencyGraph()
    g.add_node("A")
    assert g.has_cycle() is False
    assert g.get_cycle_nodes() is None
