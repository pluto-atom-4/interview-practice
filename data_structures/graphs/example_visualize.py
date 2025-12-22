"""
Example: Visualize Graph from graph.py
=======================================

This script demonstrates how to use the visualization with the Graph class
and the edges defined in graph.py line 144.
"""

from graph import Graph
from visualize_graph import visualize_graph_object

# Edges from graph.py line 144
edges = [("A", "B"), ("A", "C"), ("B", "D"), ("C", "D"), ("D", "E")]

# Create and populate the graph
g: Graph[str] = Graph[str](directed=False)
for src, dest in edges:
    g.add_edge(src, dest)

print(f"Graph created: {g!r}\n")
print("Adjacency List:")
print(g)
print("\n" + "=" * 50)

# Visualize with different layouts
layouts = ["spring", "circular", "kamada_kawai"]

for layout_name in layouts:
    print(f"\nGenerating {layout_name} layout visualization...")
    visualize_graph_object(
        g,
        layout=layout_name,
        title=f"Graph Visualization - {layout_name.capitalize()} Layout",
    )

