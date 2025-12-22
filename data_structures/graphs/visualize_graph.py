"""
Graph Visualization Script
==========================

Visualizes graph structures using networkx and matplotlib.
Provides multiple layout algorithms for different visualization styles.

Usage:
    from visualize_graph import visualize_edges

    edges = [("A", "B"), ("A", "C"), ("B", "D"), ("C", "D"), ("D", "E")]
    visualize_edges(edges, directed=False)
"""

from __future__ import annotations

from typing import Sequence

try:
    import matplotlib.pyplot as plt
    import networkx as nx
except ImportError as e:
    raise ImportError(
        "Required packages not found. Install with: pip install networkx matplotlib"
    ) from e


def visualize_edges(
    edges: Sequence[tuple],
    directed: bool = False,
    layout: str = "spring",
    title: str | None = None,
    figsize: tuple[int, int] = (10, 8),
    node_size: int = 1500,
    font_size: int = 12,
    show: bool = True,
) -> None:
    """Visualize a graph from a list of edges.

    Args:
        edges: List of tuples representing edges (src, dest).
        directed: If True, create directed graph; otherwise undirected.
        layout: Layout algorithm to use. Options: "spring", "circular", "random", "shell".
        title: Title for the visualization (auto-generated if None).
        figsize: Figure size as (width, height).
        node_size: Size of nodes in the visualization.
        font_size: Size of node labels.
        show: If True, display the graph; if False, return axes.
    """
    # Create graph
    graph_class = nx.DiGraph if directed else nx.Graph
    G = graph_class()

    # Add edges
    G.add_edges_from(edges)

    # Choose layout
    layouts = {
        "spring": nx.spring_layout,
        "circular": nx.circular_layout,
        "random": nx.random_layout,
        "shell": lambda g: nx.shell_layout(g),
        "kamada_kawai": nx.kamada_kawai_layout,
    }

    layout_func = layouts.get(layout, nx.spring_layout)
    pos = layout_func(G)

    # Create figure
    plt.figure(figsize=figsize)

    # Draw graph
    nx.draw_networkx_nodes(
        G, pos, node_color="lightblue", node_size=node_size, edgecolors="navy"
    )
    nx.draw_networkx_labels(G, pos, font_size=font_size, font_weight="bold")

    # Draw edges with arrows for directed graphs
    if directed:
        nx.draw_networkx_edges(G, pos, edge_color="gray", arrows=True, arrowsize=20)
    else:
        nx.draw_networkx_edges(G, pos, edge_color="gray")

    # Set title and clean up axes
    graph_type = "Directed Graph" if directed else "Undirected Graph"
    if title is None:
        title = f"{graph_type} ({len(G.nodes)} nodes, {len(G.edges)} edges)"

    plt.title(title, fontsize=14, fontweight="bold")
    plt.axis("off")
    plt.tight_layout()

    if show:
        plt.show()


def visualize_graph_object(graph, title: str | None = None, **kwargs) -> None:
    """Visualize a Graph object.

    Args:
        graph: Graph object with adj_list and directed attributes.
        title: Title for the visualization.
        **kwargs: Additional arguments passed to visualize_edges.
    """
    # Extract edges from adjacency list
    edges = []
    seen = set()

    for node, neighbors in graph.adj_list.items():
        for neighbor in neighbors:
            # For undirected graphs, avoid duplicate edges
            if graph.directed or (node, neighbor) not in seen and (neighbor, node) not in seen:
                edges.append((node, neighbor))
                if not graph.directed:
                    seen.add((node, neighbor))

    if title is None:
        title = f"Graph Visualization - {graph!r}"

    visualize_edges(edges, directed=graph.directed, title=title, **kwargs)


if __name__ == "__main__":
    # Example usage with the edges from graph.py
    example_edges = [("A", "B"), ("A", "C"), ("B", "D"), ("C", "D"), ("D", "E")]

    print("Visualizing undirected graph with spring layout...")
    visualize_edges(example_edges, directed=False, layout="spring")

    print("\nVisualizing undirected graph with circular layout...")
    visualize_edges(example_edges, directed=False, layout="circular")

    # Optional: Test with Graph object from graph.py
    print("\nTesting with Graph object...")
    try:
        from graph import Graph

        g = Graph[str](directed=False)
        for src, dest in example_edges:
            g.add_edge(src, dest)

        visualize_graph_object(g, layout="spring")
    except ImportError:
        print("Graph class not available for this test")

