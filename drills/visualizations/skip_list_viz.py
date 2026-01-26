from __future__ import annotations

from manim import (
    DOWN,
    LEFT,
    ORIGIN,
    RIGHT,
    UP,
    Arrow,
    Create,
    Rectangle,
    Scene,
    Text,
    VGroup,
)


class SkipListVisualization(Scene):
    """
    Simple static visualization of a small skip list:
    - Shows multiple levels
    - Nodes with arrows to next nodes
    This is illustrative, not dynamically built from the code.
    """

    def construct(self):
        # Level 0 nodes
        values = ["a", "b", "c", "d"]
        level0_nodes = VGroup()
        for i, v in enumerate(values):
            box = Rectangle(width=1.0, height=0.5)
            label = Text(v, font_size=24).move_to(box.get_center())
            node = VGroup(box, label).move_to(ORIGIN + RIGHT * (i * 1.5))
            level0_nodes.add(node)

        level0_nodes.shift(DOWN * 1.5)

        # Level 1 nodes (skip some)
        level1_indices = [0, 2]  # a, c
        level1_nodes = VGroup()
        for idx in level1_indices:
            v = values[idx]
            box = Rectangle(width=1.0, height=0.5, color="#00FFAA")
            label = Text(v, font_size=24).move_to(box.get_center())
            node = VGroup(box, label).move_to(
                level0_nodes[idx].get_center() + UP * 1.0
            )
            level1_nodes.add(node)

        self.play(*[Create(node) for node in level0_nodes])
        self.play(*[Create(node) for node in level1_nodes])

        # Horizontal arrows level 0
        arrows_level0 = VGroup()
        for i in range(len(level0_nodes) - 1):
            start = level0_nodes[i].get_right()
            end = level0_nodes[i + 1].get_left()
            arrows_level0.add(Arrow(start, end, buff=0.1))

        # Horizontal arrows level 1
        arrows_level1 = VGroup()
        for i in range(len(level1_nodes) - 1):
            start = level1_nodes[i].get_right()
            end = level1_nodes[i + 1].get_left()
            arrows_level1.add(Arrow(start, end, buff=0.1, color="#00FFAA"))

        # Vertical arrows
        vertical_arrows = VGroup()
        for i, idx in enumerate(level1_indices):
            start = level1_nodes[i].get_bottom()
            end = level0_nodes[idx].get_top()
            vertical_arrows.add(Arrow(start, end, buff=0.1))

        self.play(*[Create(a) for a in arrows_level0])
        self.play(*[Create(a) for a in arrows_level1])
        self.play(*[Create(a) for a in vertical_arrows])

        title = Text("Skip List (Redis-style sorted set)", font_size=28).to_edge(UP)
        self.play(Create(title))
        self.wait(2)
