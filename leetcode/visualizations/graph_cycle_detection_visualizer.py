import math

from manim import *


class GraphCycleDetectionVisualizer(Scene):
    """
    Visualizes cycle detection using Union–Find.
    Edges are added one by one.
    If an edge connects two nodes already in the same set, a cycle is shown.
    """

    def construct(self):
        # Example graph with a cycle:
        # 0 -- 1 -- 2
        #  \        /
        #    ------
        edges = [(0, 1), (1, 2), (2, 0)]
        n = 3

        # Layout nodes in a triangle
        node_positions = {
            0: LEFT * 2 + DOWN * 1,
            1: RIGHT * 2 + DOWN * 1,
            2: UP * 2,
        }

        # Draw nodes
        nodes = self.draw_nodes(node_positions)
        self.play(*[FadeIn(n) for n in nodes.values()])
        self.wait(1)

        # Initialize Union–Find
        parent = list(range(n))

        def find(x):
            while parent[x] != x:
                x = parent[x]
            return x

        # Process edges with animation
        for a, b in edges:
            rootA, rootB = find(a), find(b)

            edge_line = Line(node_positions[a], node_positions[b], color=GRAY)

            # Show the edge being considered
            self.play(Create(edge_line))
            self.wait(0.5)

            if rootA == rootB:
                # Cycle detected — highlight in RED
                cycle_text = Text("Cycle detected!", color=RED).to_edge(UP)
                self.play(edge_line.animate.set_color(RED), FadeIn(cycle_text))
                self.wait(2)
                self.play(FadeOut(cycle_text))
            else:
                # No cycle — union the sets
                union_text = Text(f"Union({a}, {b})", color=GREEN).to_edge(UP)
                self.play(FadeIn(union_text))
                self.wait(0.5)

                # Union by setting parent
                parent[rootB] = rootA

                self.play(FadeOut(union_text))

        self.wait(2)

    # ---------------------------------------------------------
    # Helper: draw nodes
    # ---------------------------------------------------------

    def draw_nodes(self, positions):
        nodes = {}
        for i, pos in positions.items():
            circle = Circle(radius=0.4, color=BLUE).move_to(pos)
            label = Text(str(i), font_size=28).move_to(circle.get_center())
            nodes[i] = VGroup(circle, label)
        return nodes
