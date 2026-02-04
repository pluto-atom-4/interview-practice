"""
FUNCTION graph_lowest_common_ancestor(graph, root, p, q):
    RETURN dfs(root)

    INNER FUNCTION dfs(node):
        // Base case: return node if it is one of the targets or a dead end
        IF node is null OR node == p OR node == q:
            RETURN node

        INITIALIZE found_nodes as empty list

        // Explore all reachable neighbors (children)
        FOR EACH (neighbor, weight) IN graph.adj_list[node]:
            result = dfs(neighbor)

            // If the target was found in this branch, track it
            IF result is not null:
                APPEND result TO found_nodes

        // If targets are found in different sub-branches, this node is the LCA
        IF length of found_nodes >= 2:
            RETURN node

        // Otherwise, pass up the single result found, or null if nothing was found
        IF found_nodes is not empty:
            RETURN found_nodes[0]
        ELSE:
            RETURN null
"""


from drills.find_lowest_common_ancestor import graph_lowest_common_ancestor
from drills.graph import Graph


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