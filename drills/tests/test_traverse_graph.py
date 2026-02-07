import pytest

from drills.graph import Graph
from drills.traverse_graph import graph_bfs, graph_dfs

"""
FUNCTION graph_bfs(graph, start_node):
    INITIALIZE visited as an empty set
    INITIALIZE queue as a double-ended queue containing [start_node]
    
    ADD start_node TO visited

    WHILE queue is not empty:
        vertex = REMOVE from front of queue (popleft)
        YIELD vertex  // Produce the current node lazily

        FOR each (neighbor, weight) in graph's adjacency list for vertex:
            IF neighbor is NOT in visited:
                ADD neighbor TO visited
                ADD neighbor TO the end of queue (append)
"""
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


