import pytest


from leetcode.is_graph_bipartite import is_bipartite



@pytest.mark.parametrize(
    "graph, expected",
    [
        # Basic case: simple bipartite graph
        ([[1], [0, 3], [3], [1, 2]], True),
        # Graph with odd cycle (not bipartite)
        ([[1, 2], [0, 2], [0, 1]], False),
        # Disconnected graph with one component bipartite and one not
        ([[1], [0], [3], [2]], True),
        # Empty graph (trivially bipartite)
        ([], True),
        # Graph with self-loop (not bipartite)
        ([[0]], False),
        # Graph with multiple components, all bipartite
        ([[1], [0], [3], [2]], True),
    ]
)
def test_is_bipartite(graph, expected):
    assert is_bipartite(graph) == expected
