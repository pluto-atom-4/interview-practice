"""
Test suite for drills.graph module.

Tests cover Graph class initialization, edge addition,
adjacency list representation, and basic graph operations.
"""

import pytest

from drills.detect_graph_cycle import graph_cycle_detection
from drills.find_lowest_common_ancestor import graph_lowest_common_ancestor
from drills.graph import Graph
from drills.topological_sort_graph import graph_topological_sort
from drills.traverse_graph import graph_bfs, graph_dfs


class TestGraphInitialization:
    """Test Graph initialization and basic properties."""

    def test_graph_initialization_undirected(self):
        """Test creating an undirected graph."""
        graph = Graph()
        assert graph.directed is False
        assert len(graph.adj_list) == 0

    def test_graph_initialization_directed(self):
        """Test creating a directed graph."""
        graph = Graph(directed=True)
        assert graph.directed is True
        assert len(graph.adj_list) == 0

    def test_graph_with_int_vertices(self):
        """Test graph with integer vertices."""
        graph = Graph[int]()
        assert graph.directed is False

    def test_graph_with_string_vertices(self):
        """Test graph with string vertices."""
        graph = Graph[str]()
        assert graph.directed is False

class TestGraphBasicOperations:
    """Test basic graph operations like adding edges and size. """

    def test_graph_size_empty(self):
        graph = Graph()
        assert graph.size() == 0

    def test_graph_size_after_adding_vertices(self):
        graph = Graph()
        graph.add_vertex("A")
        graph.add_vertex("B")
        assert graph.size() == 2

class TestGraphAddEdge:
    """ Test adding edges to the graph. """

    def test_graph_add_edge_empty(self):
        graph = Graph()
        graph.add_edge("A", "B", 1)
        assert "B" in [dest for dest, weight in graph.adj_list["A"]]
        assert "A" in [dest for dest, weight in graph.adj_list["B"]]

    def test_graph_add_edge_existing_vertices(self):
        graph = Graph()
        graph.add_vertex("A")
        graph.add_vertex("B")
        graph.add_edge("A", "B", 1)
        assert "B" in [dest for dest, weight in graph.adj_list["A"]]
        assert "A" in [dest for dest, weight in graph.adj_list["B"]]
    def test_graph_add_edge_directed(self):
        graph = Graph(directed=True)
        graph.add_edge("A", "B", 1)
        assert "B" in [dest for dest, weight in graph.adj_list["A"]]
        assert "A" not in [dest for dest, weight in graph.adj_list["B"]]
    def test_graph_add_edge_with_weight(self):
        graph = Graph()
        graph.add_edge("A", "B", 5)
        assert ( "B", 5) in graph.adj_list["A"]
        assert ( "A", 5) in graph.adj_list["B"]
    def test_graph_add_multiple_edges(self):
        graph = Graph()
        graph.add_edge("A", "B", 1)
        graph.add_edge("A", "C", 2)
        graph.add_edge("B", "C", 3)
        assert len(graph.adj_list["A"]) == 2
        assert len(graph.adj_list["B"]) == 2
        assert len(graph.adj_list["C"]) == 2
    def test_graph_add_self_loop(self):
        graph = Graph()
        graph.add_edge("A", "A", 1)
        assert ("A", 1) in graph.adj_list["A"]
    def test_graph_add_duplicate_edge(self):
        graph = Graph()
        graph.add_edge("A", "B", 1)
        graph.add_edge("A", "B", 1)
        edges = [dest for dest, weight in graph.adj_list["A"] if dest == "B"]
        assert len(edges) == 1

class TestRemoveEdge:
    """ Test removing edges from the graph. """

    def test_graph_remove_edge_existing(self):
        graph = Graph()
        graph.add_edge("A", "B", 1)
        graph.remove_edge("A", "B", 1)
        assert "B" not in [dest for dest, weight in graph.adj_list["A"]]
        assert "A" not in [dest for dest, weight in graph.adj_list["B"]]

    def test_graph_remove_edge_non_existing(self):
        graph = Graph()
        graph.add_edge("A", "B", 1)
        graph.remove_edge("A", "C", 1)  # Removing non-existing edge
        assert "B" in [dest for dest, weight in graph.adj_list["A"]]
        assert "A" in [dest for dest, weight in graph.adj_list["B"]]

class TestRemoveDependentVertex:
    """ Test removing vertices from the graph. """

    def test_graph_remove_vertex_existing(self):
        graph = Graph()
        graph.add_edge("A", "B", 1)
        graph.remove_vertex("A")
        assert "A" not in graph.adj_list
        assert "A" not in [dest for dest, weight in graph.adj_list["B"]]

    def test_graph_remove_vertex_non_existing(self):
        graph = Graph()
        graph.add_edge("A", "B", 1)
        graph.remove_vertex("C")  # Removing non-existing vertex
        assert "A" in graph.adj_list
        assert "B" in graph.adj_list
    
    def test_graph_remove_vertex_with_multiple_edges(self):
        graph = Graph()
        graph.add_edge("A", "B", 1)
        graph.add_edge("A", "C", 2)
        graph.add_edge("B", "C", 3)
        graph.remove_vertex("A")
        assert "A" not in graph.adj_list
        assert "A" not in [dest for dest, weight in graph.adj_list["B"]]
        assert "A" not in [dest for dest, weight in graph.adj_list["C"]]

    def test_graph_remove_vertex_self_loop(self):
        graph = Graph()
        graph.add_edge("A", "A", 1)
        graph.remove_vertex("A")
        assert "A" not in graph.adj_list
    
    def test_graph_remove_dependent_vertex(self):
        graph = Graph()
        graph.add_edge("A", "B", 1)
        graph.add_edge("B", "C", 2)
        graph.remove_vertex("B")
        assert "B" not in graph.adj_list
        assert "B" not in [dest for dest, weight in graph.adj_list["A"]]
        assert "B" not in [dest for dest, weight in graph.adj_list["C"]]

class TestGraphBFS:
    """ Test BFS traversal of the graph. """

    def test_graph_bfs_traversal(self):
        graph = Graph()
        graph.add_edge("A", "B", 1)
        graph.add_edge("A", "C", 1)
        graph.add_edge("B", "D", 1)
        graph.add_edge("C", "D", 1)
        bfs_order = list(graph_bfs(graph, "A"))
        assert bfs_order == ["A", "B", "C", "D"]

    def test_graph_bfs_single_vertex(self):
        graph = Graph()
        graph.add_vertex("A")
        bfs_order = list(graph_bfs(graph, "A"))
        assert bfs_order == ["A"]
        
    def test_graph_bfs_disconnected(self):
        graph = Graph()
        graph.add_edge("A", "B", 1)
        graph.add_vertex("C")  # Disconnected vertex
        bfs_order = list(graph_bfs(graph, "A"))
        assert bfs_order == ["A", "B"]

class TestGraphDFS:
    """ Test DFS traversal of the graph. """

    def test_graph_dfs_traversal(self):
        graph = Graph()
        graph.add_edge("A", "B", 1)
        graph.add_edge("A", "C", 1)
        graph.add_edge("B", "D", 1)
        graph.add_edge("C", "D", 1)
        dfs_order = list(graph_dfs(graph, "A"))
        assert dfs_order == ["A", "C", "D", "B"] or dfs_order == ["A", "B", "D", "C"]

    def test_graph_dfs_single_vertex(self):
        graph = Graph()
        graph.add_vertex("A")
        dfs_order = list(graph_dfs(graph, "A"))
        assert dfs_order == ["A"]

    def test_graph_dfs_disconnected(self):
        graph = Graph()
        graph.add_edge("A", "B", 1)
        graph.add_vertex("C")  # Disconnected vertex
        dfs_order = list(graph_dfs(graph, "A"))
        assert dfs_order == ["A", "B"]

class TestGraphTopologicalSort:
    """ Test topological sorting of the graph. """

    def test_graph_topological_sort(self):
        graph = Graph(directed=True)
        graph.add_edge("A", "B", 1)
        graph.add_edge("B", "C", 1)
        graph.add_edge("A", "C", 1)
        topo_order = graph_topological_sort(graph)
        assert topo_order.index("A") < topo_order.index("B") < topo_order.index("C")

    def test_graph_topological_sort_no_edges(self):
        graph = Graph(directed=True)
        graph.add_vertex("A")
        graph.add_vertex("B")
        graph.add_vertex("C")
        topo_order = graph_topological_sort(graph)
        assert set(topo_order) == {"A", "B", "C"}

class TestGraphLowestCommonAncestor:
    """ Test lowest common ancestor in the graph. """

    def test_graph_lowest_common_ancestor(self):
        graph = Graph(directed=True)
        graph.add_edge("A", "B", 1)
        graph.add_edge("A", "C", 1)
        graph.add_edge("B", "D", 1)
        graph.add_edge("C", "D", 1)
        lca = graph_lowest_common_ancestor(graph, "A", "B", "C")
        assert lca == "A"

    def test_graph_lowest_common_ancestor_no_common(self):
        graph = Graph(directed=True)
        graph.add_edge("A", "B", 1)
        graph.add_edge("C", "D", 1)
        lca = graph_lowest_common_ancestor(graph, "B", "D", "C")
        assert lca is None