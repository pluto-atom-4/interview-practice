"""
FUNCTION graph_cycle_detection(graph):
    CREATE an empty set named visited (to track fully processed nodes)
    CREATE an empty set named rec_stack (to track nodes in current recursion path)

    FUNCTION dfs(v):
        ADD v to visited set
        ADD v to rec_stack set (node is now in active path)

        FOR EACH neighbor OF v:
            IF neighbor is NOT in visited:
                IF dfs(neighbor) returns True:
                    RETURN True
            ELSE IF neighbor is in rec_stack:
                RETURN True (cycle detected via back edge)

        REMOVE v from rec_stack (backtracking: node no longer in active path)
        RETURN False

    FOR EACH vertex IN graph:
        IF vertex is NOT in visited:
            IF dfs(vertex) returns True:
                RETURN True

    RETURN False (no cycles found)
 
"""

from drills.detect_graph_cycle import graph_cycle_detection
from drills.graph import Graph


class TestGraphCycles:
    """Test graph cycle detection using modern Python style."""

    def test_graph_cycle_detection(self):
        graph = Graph(directed=True)
        graph.add_edge("A", "B", 1)
        graph.add_edge("B", "C", 1)
        graph.add_edge("C", "A", 1)  # Creates a cycle: A -> B -> C -> A
        assert "B" in [dest for dest, _ in graph.adj_list["A"]]
        assert "C" in [dest for dest, _ in graph.adj_list["B"]]
        assert "A" in [dest for dest, _ in graph.adj_list["C"]]
        assert graph_cycle_detection(graph) is True

    def test_graph_no_cycle_detection(self):
        graph = Graph(directed=True)
        graph.add_edge("A", "B", 1)
        graph.add_edge("B", "C", 1)
        assert "B" in [dest for dest, _ in graph.adj_list["A"]]
        assert "C" in [dest for dest, _ in graph.adj_list["B"]]
        assert graph_cycle_detection(graph) is False

    def test_graph_cycle_detection_self_loop(self):
        graph = Graph(directed=True)
        graph.add_edge("A", "A", 1)  # Self-loop creates a cycle
        assert ("A", 1) in graph.adj_list["A"]
        assert graph_cycle_detection(graph) is True
