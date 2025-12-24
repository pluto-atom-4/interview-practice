import math
from typing import List, Optional

from manim import *


class ArrayBinaryTreeVisualizer(Scene):
    """
    Visualizes how an array-backed binary tree stores nodes.
    Produces animations showing:
      - the array layout
      - the tree structure
      - index relationships (parent, left, right)
    """

    def construct(self):
        # Example tree values
        values = [10, 20, 30, 40, 50, None, 70]

        # Draw array representation
        array_group = self.draw_array(values)
        self.play(FadeIn(array_group))
        self.wait(1)

        # Draw tree representation
        tree_group = self.draw_tree(values)
        self.play(FadeIn(tree_group))
        self.wait(1)

        # Connect array indices to tree nodes
        connectors = self.connect_array_to_tree(array_group, tree_group, values)
        self.play(*[Create(line) for line in connectors])
        self.wait(2)

    # ---------------------------------------------------------
    # Helpers
    # ---------------------------------------------------------

    def draw_array(self, values: List[Optional[int]]):
        boxes = []
        labels = []

        for i, v in enumerate(values):
            box = Square(side_length=1).shift(RIGHT * i)
            label = Text(str(v) if v is not None else "None", font_size=28).move_to(box.get_center())
            index = Text(str(i), font_size=20, color=YELLOW).next_to(box, DOWN, buff=0.1)

            boxes.append(VGroup(box, label, index))

        return VGroup(*boxes).shift(UP * 2.5 + LEFT * 3)

    def draw_tree(self, values: List[Optional[int]]):
        nodes = []
        positions = {}

        # Compute positions for each index
        for i, v in enumerate(values):
            if v is None:
                continue

            level = int(math.log2(i + 1))
            pos_x = (i - (2 ** level - 1)) * 1.5
            pos_y = -level * 1.5

            node = Circle(radius=0.4, color=BLUE).move_to([pos_x, pos_y, 0])
            label = Text(str(v), font_size=28).move_to(node.get_center())

            nodes.append(VGroup(node, label))
            positions[i] = node.get_center()

        # Draw edges
        edges = []
        for i in positions:
            left = 2 * i + 1
            right = 2 * i + 2

            if left in positions:
                edges.append(Line(positions[i], positions[left]))
            if right in positions:
                edges.append(Line(positions[i], positions[right]))

        return VGroup(*nodes, *edges).shift(DOWN * 1)

    def connect_array_to_tree(self, array_group, tree_group, values):
        connectors = []

        array_boxes = array_group.submobjects
        tree_nodes = [m for m in tree_group.submobjects if isinstance(m, VGroup)]

        # Map index → tree node center
        tree_positions = {}
        for node in tree_nodes:
            label = node.submobjects[1].text
            # Find index by matching value (simple demo assumption)
            for i, v in enumerate(values):
                if str(v) == label:
                    tree_positions[i] = node.get_center()

        for i, box in enumerate(array_boxes):
            if i in tree_positions:
                connectors.append(
                    Line(
                        box.get_center() + DOWN * 0.5,
                        tree_positions[i] + UP * 0.5,
                        color=GRAY
                    )
                )

        return connectors
