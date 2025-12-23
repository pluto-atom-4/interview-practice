"""
Tree Visualization Script
=========================

Visualizes tree structures using networkx and matplotlib.
Provides layout algorithms for different visualization styles.

Usage:
    from visualize_tree import visualize_tree_json, visualize_tree_object

    # Using JSON
    tree_json = {
        "value": "A",
        "children": [
            {"value": "B", "children": [{"value": "D"}, {"value": "E"}]},
            {"value": "C", "children": [{"value": "F"}]}
        ]
    }
    visualize_tree_json(tree_json)

    # Using Tree object
    from tree import Tree, TreeNode
    root = TreeNode("A")
    root.add_child(TreeNode("B"))
    tree = Tree(root)
    visualize_tree_object(tree)
"""

from __future__ import annotations

import json
from typing import Any, Optional

try:
    import matplotlib.pyplot as plt
    import networkx as nx
except ImportError as e:
    raise ImportError(
        "Required packages not found. Install with: pip install networkx matplotlib"
    ) from e


def visualize_tree_json(
    tree_json: dict[str, Any] | str,
    title: str | None = None,
    figsize: tuple[int, int] = (12, 8),
    node_size: int = 1500,
    font_size: int = 11,
    show: bool = True,
) -> None:
    """Visualize a tree from a JSON object or JSON string.

    Args:
        tree_json: Tree structure as a dictionary or JSON string.
                   Expected format: {"value": "root", "children": [{"value": "child1", "children": [...]}, ...]}
        title: Title for the visualization (auto-generated if None).
        figsize: Figure size as (width, height).
        node_size: Size of nodes in the visualization.
        font_size: Size of node labels.
        show: If True, display the tree; if False, return axes.

    Raises:
        ValueError: If tree_json format is invalid.
    """
    # Parse JSON string if needed
    if isinstance(tree_json, str):
        try:
            tree_json = json.loads(tree_json)
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON string: {e}") from e

    if not isinstance(tree_json, dict) or "value" not in tree_json:
        raise ValueError("Invalid tree format. Expected {'value': ..., 'children': [...]}")

    # Build networkx tree
    G = nx.DiGraph()
    node_counter = [0]  # Use list to allow modification in nested function

    def add_nodes_edges(node_data: dict[str, Any], parent_id: Optional[str] = None) -> str:
        """Recursively add nodes and edges to the graph."""
        node_id = f"node_{node_counter[0]}"
        node_counter[0] += 1

        value = node_data.get("value", "")
        G.add_node(node_id, label=str(value))

        if parent_id is not None:
            G.add_edge(parent_id, node_id)

        # Process children
        for child in node_data.get("children", []):
            add_nodes_edges(child, node_id)

        return node_id

    root_id = add_nodes_edges(tree_json)

    # Use hierarchical layout for trees
    pos = _hierarchy_pos(G, root_id, vert_gap=2, vert_loc=0)

    # Create figure
    plt.figure(figsize=figsize)

    # Draw nodes
    nx.draw_networkx_nodes(
        G, pos, node_color="lightgreen", node_size=node_size, edgecolors="darkgreen"
    )

    # Draw labels
    labels = nx.get_node_attributes(G, "label")
    nx.draw_networkx_labels(G, pos, labels, font_size=font_size, font_weight="bold")

    # Draw edges with arrows
    nx.draw_networkx_edges(G, pos, edge_color="gray", arrows=True, arrowsize=20)

    # Set title and clean up axes
    if title is None:
        title = f"Tree Visualization ({len(G.nodes)} nodes)"

    plt.title(title, fontsize=14, fontweight="bold")
    plt.axis("off")
    plt.tight_layout()

    if show:
        plt.show()


def visualize_tree_object(
    tree,
    title: str | None = None,
    figsize: tuple[int, int] = (12, 8),
    node_size: int = 1500,
    font_size: int = 11,
    show: bool = True,
) -> None:
    """Visualize a Tree object.

    Args:
        tree: Tree object with root attribute (TreeNode).
        title: Title for the visualization.
        figsize: Figure size as (width, height).
        node_size: Size of nodes in the visualization.
        font_size: Size of node labels.
        show: If True, display the tree; if False, return axes.
    """
    if tree.root is None:
        raise ValueError("Tree is empty (root is None)")

    # Convert Tree to JSON structure
    tree_json = _tree_to_json(tree.root)

    if title is None:
        title = f"Tree Visualization ({_count_nodes(tree.root)} nodes)"

    visualize_tree_json(tree_json, title=title, figsize=figsize, node_size=node_size,
                       font_size=font_size, show=show)


def tree_to_json(tree) -> dict[str, Any]:
    """Convert a Tree object to JSON representation.

    Args:
        tree: Tree object with root attribute (TreeNode).

    Returns:
        Dictionary representation of the tree in JSON format.
    """
    if tree.root is None:
        return {}
    return _tree_to_json(tree.root)


def _tree_to_json(node) -> dict[str, Any]:
    """Recursively convert TreeNode to JSON format."""
    return {
        "value": node.value,
        "children": [_tree_to_json(child) for child in node.children]
    }


def _count_nodes(node) -> int:
    """Count total nodes in a tree."""
    count = 1
    for child in node.children:
        count += _count_nodes(child)
    return count


def _hierarchy_pos(
    G: nx.DiGraph,
    root: str,
    width: float = 1.0,
    vert_gap: float = 0.2,
    vert_loc: float = 0,
    xcenter: float = 0.5,
) -> dict[str, tuple[float, float]]:
    """
    Create hierarchical tree layout positions.

    This function computes positions for a tree layout using a recursive approach.
    It's adapted from networkx community for tree-like structures.

    Args:
        G: NetworkX directed graph (tree).
        root: Root node of the tree.
        width: Width of the tree layout.
        vert_gap: Vertical gap between levels.
        vert_loc: Vertical location of the root.
        xcenter: Horizontal center position.

    Returns:
        Dictionary mapping nodes to (x, y) positions.
    """
    pos = {root: (xcenter, vert_loc)}
    neighbors = list(G.neighbors(root))

    if len(neighbors) != 0:
        dx = width / len(neighbors)
        nextx = xcenter - width / 2 - dx / 2
        for neighbor in neighbors:
            nextx += dx
            pos.update(
                _hierarchy_pos(
                    G,
                    neighbor,
                    width=dx,
                    vert_gap=vert_gap,
                    vert_loc=vert_loc - vert_gap,
                    xcenter=nextx,
                )
            )

    return pos


if __name__ == "__main__":
    # Example 1: Visualize from JSON dict
    print("Example 1: Visualizing tree from JSON dictionary...")
    tree_json = {
        "value": "A",
        "children": [
            {
                "value": "B",
                "children": [
                    {"value": "D", "children": []},
                    {"value": "E", "children": []}
                ]
            },
            {
                "value": "C",
                "children": [
                    {"value": "F", "children": []}
                ]
            }
        ]
    }
    visualize_tree_json(tree_json)

    # Example 2: Visualize from JSON string
    print("\nExample 2: Visualizing tree from JSON string...")
    tree_json_str = json.dumps(tree_json)
    visualize_tree_json(tree_json_str, title="Tree from JSON String")

    # Example 3: Visualize Tree object
    print("\nExample 3: Visualizing Tree object...")
    try:
        from tree import Tree, TreeNode

        root = TreeNode("Root")
        child1 = TreeNode("Child1")
        child2 = TreeNode("Child2")
        grandchild1 = TreeNode("GrandChild1")
        grandchild2 = TreeNode("GrandChild2")

        root.add_child(child1)
        root.add_child(child2)
        child1.add_child(grandchild1)
        child1.add_child(grandchild2)

        tree = Tree(root)
        visualize_tree_object(tree)
    except ImportError:
        print("Tree class not available for this test")

