"""
Advanced Manim Tree Visualization for Level-Order Parsing
==========================================================

Enhanced animations showing:
1. Dynamic tree construction with edges
2. Animated node highlighting for level-order traversal
3. Real-time precedence visualization
4. Interactive tree manipulation

Usage:
    manim -pql manim_advanced_trees.py TreeBuildingVisualization
    manim -pql manim_advanced_trees.py PrecedenceComparison
    manim -pql manim_advanced_trees.py DynamicTreeGrowth
"""

import os
from typing import Dict, List, Tuple

from manim import config

# Set media directory to [project root]/generated/media
config.media_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../generated/media'))

import numpy as np
from manim import *


class TreeNode(VGroup):
    """Custom tree node with label and customizable styling."""

    def __init__(self, value: str, node_type: str = "operand", **kwargs):
        super().__init__(**kwargs)
        self.value = value
        self.node_type = node_type

        # Color based on type
        color = GREEN if node_type == "operand" else RED

        circle = Circle(radius=0.35, color=color, fill_opacity=0.8)
        text = Text(str(value), font_size=20, color=WHITE)

        # Center text on circle
        text.move_to(circle.get_center())

        self.add(circle, text)
        self.circle = circle
        self.text = text
        self.children_nodes = []

    def highlight(self, color=YELLOW):
        """Highlight this node."""
        self.circle.set_color(color)

    def reset_color(self):
        """Reset to original color."""
        color = GREEN if self.node_type == "operand" else RED
        self.circle.set_color(color)


class TreeBuildingVisualization(Scene):
    """Show tree building process with edges appearing as children are added."""

    def construct(self):
        title = Text("Building Expression Tree: 2 + 3 * 4", font_size=36, color=BLUE)
        title.to_edge(UP)
        self.add(title)

        # Create nodes with positions
        root = TreeNode("+", "operator")
        root.shift(UP * 2)

        left = TreeNode("2", "operand")
        left.shift(LEFT * 3 + DOWN * 1)

        right = TreeNode("*", "operator")
        right.shift(RIGHT * 3 + DOWN * 1)

        left_left = TreeNode("3", "operand")
        left_left.shift(LEFT * 4.5 + DOWN * 3)

        left_right = TreeNode("4", "operand")
        left_right.shift(RIGHT * 1.5 + DOWN * 3)

        # Stage 1: Add root
        step1_text = Text("Step 1: Create root operator", font_size=18, color=CYAN)
        step1_text.to_edge(DOWN)
        self.play(Write(step1_text))
        self.play(Create(root), run_time=1)
        self.wait(1)

        # Stage 2: Add left child
        step2_text = Text("Step 2: Add left operand", font_size=18, color=CYAN)
        self.play(Transform(step1_text, step2_text))
        self.play(Create(left), run_time=0.8)
        line1 = Line(root.get_center(), left.get_center(), color=BLUE, stroke_width=3)
        self.play(Create(line1), run_time=0.8)
        self.wait(0.5)

        # Stage 3: Add right child
        step3_text = Text("Step 3: Add right operator", font_size=18, color=CYAN)
        self.play(Transform(step1_text, step3_text))
        self.play(Create(right), run_time=0.8)
        line2 = Line(root.get_center(), right.get_center(), color=BLUE, stroke_width=3)
        self.play(Create(line2), run_time=0.8)
        self.wait(0.5)

        # Stage 4: Add children of right node
        step4_text = Text("Step 4: Add children of right operator", font_size=18, color=CYAN)
        self.play(Transform(step1_text, step4_text))
        self.play(Create(left_left), run_time=0.8)
        line3 = Line(right.get_center(), left_left.get_center(), color=BLUE, stroke_width=3)
        self.play(Create(line3), run_time=0.8)
        self.wait(0.3)

        self.play(Create(left_right), run_time=0.8)
        line4 = Line(right.get_center(), left_right.get_center(), color=BLUE, stroke_width=3)
        self.play(Create(line4), run_time=0.8)
        self.wait(1)

        # Highlight complete tree
        complete_text = Text("Complete Tree!", font_size=18, color=GREEN)
        self.play(Transform(step1_text, complete_text))

        # Pulse all nodes
        for node in [root, left, right, left_left, left_right]:
            self.play(node.circle.animate.scale(1.2), run_time=0.2)
            self.play(node.circle.animate.scale(1 / 1.2), run_time=0.2)

        self.wait(2)


class PrecedenceComparison(Scene):
    """Compare two expressions showing how precedence affects tree structure."""

    def construct(self):
        title = Text("Operator Precedence Effect", font_size=40, color=BLUE)
        title.to_edge(UP)
        self.add(title)

        # Left side: 2 + 3 * 4
        expr1_text = Text("2 + 3 * 4 = 14", font_size=24, color=YELLOW)
        expr1_text.shift(LEFT * 3.5 + UP * 2)
        self.play(Write(expr1_text))

        # Left tree
        root1 = TreeNode("+", "operator")
        root1.shift(LEFT * 3.5 + UP * 0.5)

        left1 = TreeNode("2", "operand")
        left1.shift(LEFT * 5 + DOWN * 1)

        right1 = TreeNode("*", "operator")
        right1.shift(LEFT * 2 + DOWN * 1)

        left_left1 = TreeNode("3", "operand")
        left_left1.shift(LEFT * 3 + DOWN * 2.5)

        left_right1 = TreeNode("4", "operand")
        left_right1.shift(LEFT * 1 + DOWN * 2.5)

        # Draw left tree
        self.play(Create(root1), Create(left1), Create(right1))
        self.play(Create(left_left1), Create(left_right1))

        lines1 = [
            Line(root1.get_center(), left1.get_center(), color=BLUE),
            Line(root1.get_center(), right1.get_center(), color=BLUE),
            Line(right1.get_center(), left_left1.get_center(), color=BLUE),
            Line(right1.get_center(), left_right1.get_center(), color=BLUE),
        ]

        for line in lines1:
            self.play(Create(line), run_time=0.3)

        self.wait(1)

        # Right side: (2 + 3) * 4
        expr2_text = Text("(2 + 3) * 4 = 20", font_size=24, color=YELLOW)
        expr2_text.shift(RIGHT * 3.5 + UP * 2)
        self.play(Write(expr2_text))

        # Right tree (different structure due to parentheses)
        root2 = TreeNode("*", "operator")
        root2.shift(RIGHT * 3.5 + UP * 0.5)

        left2 = TreeNode("+", "operator")
        left2.shift(RIGHT * 2 + DOWN * 1)

        right2 = TreeNode("4", "operand")
        right2.shift(RIGHT * 5 + DOWN * 1)

        left_left2 = TreeNode("2", "operand")
        left_left2.shift(RIGHT * 0.5 + DOWN * 2.5)

        left_right2 = TreeNode("3", "operand")
        left_right2.shift(RIGHT * 3.5 + DOWN * 2.5)

        # Draw right tree
        self.play(Create(root2), Create(left2), Create(right2))
        self.play(Create(left_left2), Create(left_right2))

        lines2 = [
            Line(root2.get_center(), left2.get_center(), color=BLUE),
            Line(root2.get_center(), right2.get_center(), color=BLUE),
            Line(left2.get_center(), left_left2.get_center(), color=BLUE),
            Line(left2.get_center(), left_right2.get_center(), color=BLUE),
        ]

        for line in lines2:
            self.play(Create(line), run_time=0.3)

        self.wait(1)

        # Explanation
        explanation = Text(
            "Different tree structures due to parentheses!",
            font_size=20,
            color=CYAN
        )
        explanation.shift(DOWN * 3.5)
        self.play(Write(explanation))

        self.wait(2)


class LevelOrderAnimationAdvanced(Scene):
    """Animate level-order traversal with highlighting."""

    def construct(self):
        title = Text("Level-Order Traversal (BFS)", font_size=40, color=BLUE)
        title.to_edge(UP)
        self.add(title)

        # Create tree: 2 + 3 * 4
        root = TreeNode("+", "operator")
        root.shift(UP * 1.5)

        left = TreeNode("2", "operand")
        left.shift(LEFT * 2 + DOWN * 0.5)

        right = TreeNode("*", "operator")
        right.shift(RIGHT * 2 + DOWN * 0.5)

        left_left = TreeNode("3", "operand")
        left_left.shift(LEFT * 3 + DOWN * 2)

        left_right = TreeNode("4", "operand")
        left_right.shift(RIGHT * 1 + DOWN * 2)

        # Create all nodes
        for node in [root, left, right, left_left, left_right]:
            self.play(Create(node), run_time=0.3)

        # Create edges
        edges = [
            Line(root.get_center(), left.get_center(), color=BLUE),
            Line(root.get_center(), right.get_center(), color=BLUE),
            Line(right.get_center(), left_left.get_center(), color=BLUE),
            Line(right.get_center(), left_right.get_center(), color=BLUE),
        ]

        for edge in edges:
            self.play(Create(edge), run_time=0.3)

        self.wait(1)

        # Level-order traversal animation
        level_text = Text("Traversal Order:", font_size=20, color=CYAN)
        level_text.shift(DOWN * 3)
        self.play(Write(level_text))

        # Level 0
        self.play(root.circle.animate.set_color(YELLOW), run_time=0.5)
        self.wait(0.3)
        self.play(root.circle.animate.set_color(RED), run_time=0.3)

        # Level 1
        self.play(left.circle.animate.set_color(YELLOW), right.circle.animate.set_color(YELLOW), run_time=0.5)
        self.wait(0.3)
        self.play(left.circle.animate.set_color(GREEN), right.circle.animate.set_color(RED), run_time=0.3)

        # Level 2
        self.play(left_left.circle.animate.set_color(YELLOW), left_right.circle.animate.set_color(YELLOW), run_time=0.5)
        self.wait(0.3)
        self.play(left_left.circle.animate.set_color(GREEN), left_right.circle.animate.set_color(GREEN), run_time=0.3)

        # Show order
        order_text = Text("Order: + → 2 → * → 3 → 4", font_size=18, color=GREEN)
        order_text.shift(DOWN * 3.5)
        self.play(Write(order_text))

        self.wait(2)


class DynamicTreeGrowth(Scene):
    """Show tree growing dynamically as postfix tokens are processed."""

    def construct(self):
        title = Text("Tree Growth: Processing Postfix 2 3 4 * +", font_size=32, color=BLUE)
        title.to_edge(UP)
        self.add(title)

        nodes_created = []
        step_info = Text("Stack: ", font_size=16, color=YELLOW)
        step_info.shift(DOWN * 3.5)
        self.add(step_info)

        # Process tokens: 2, 3, 4, *, +
        tokens = [
            ("2", "operand", "Stack: [2]"),
            ("3", "operand", "Stack: [2, 3]"),
            ("4", "operand", "Stack: [2, 3, 4]"),
            ("*", "operator", "Stack: [2, (3*4)]"),
            ("+", "operator", "Stack: [(2+(3*4))]"),
        ]

        y_pos = 1
        x_pos = -4

        for i, (token, token_type, stack_state) in enumerate(tokens):
            # Create node
            node = TreeNode(token, token_type)
            node.shift(UP * y_pos + RIGHT * (x_pos + i * 1.5))
            nodes_created.append(node)

            # Token being processed
            token_text = Text(f"Token: {token}", font_size=18, color=CYAN)
            token_text.shift(UP * (y_pos + 2))
            self.play(Write(token_text), run_time=0.3)

            # Create node
            self.play(Create(node), run_time=0.5)

            # Update stack state
            new_step_info = Text(stack_state, font_size=16, color=YELLOW)
            new_step_info.shift(DOWN * 3.5)
            self.play(Transform(step_info, new_step_info), run_time=0.5)

            # Connect to previous nodes if operator
            if token_type == "operator" and len(nodes_created) > 1:
                right_child = nodes_created[-2]
                left_child = nodes_created[-3] if len(nodes_created) > 2 else None

                line_right = Line(node.get_center(), right_child.get_center(), color=BLUE)
                self.play(Create(line_right), run_time=0.5)

                if left_child:
                    line_left = Line(node.get_center(), left_child.get_center(), color=BLUE)
                    self.play(Create(line_left), run_time=0.5)

            self.wait(0.5)
            y_pos -= 0.8

        self.wait(2)


class ExpressionToTreeFlow(Scene):
    """Show the complete flow from expression to tree."""

    def construct(self):
        title = Text("Complete Expression Parsing Flow", font_size=40, color=BLUE)
        title.to_edge(UP)
        self.add(title)

        # Stage 1: Input expression
        expr_box = Rectangle(width=3, height=0.6, color=GREEN)
        expr_text = Text("2 + 3 * 4", font_size=20, color=WHITE)
        expr_group = VGroup(expr_box, expr_text)
        expr_group.shift(LEFT * 3 + UP * 2)

        self.play(Create(expr_box), Write(expr_text))
        stage1_label = Text("Input", font_size=14, color=YELLOW)
        stage1_label.next_to(expr_group, DOWN, buff=0.3)
        self.play(Write(stage1_label))
        self.wait(1)

        # Arrow 1
        arrow1 = Arrow(expr_group.get_bottom() + DOWN * 0.5, LEFT * 3 + DOWN * 0.5, buff=0.1, color=WHITE)
        self.play(Create(arrow1))

        # Stage 2: Tokens
        tokens_box = Rectangle(width=3, height=0.6, color=YELLOW)
        tokens_text = Text("[2, +, 3, *, 4]", font_size=14, color=WHITE)
        tokens_group = VGroup(tokens_box, tokens_text)
        tokens_group.shift(LEFT * 3 + DOWN * 0.5)

        self.play(Create(tokens_box), Write(tokens_text))
        stage2_label = Text("Tokenize", font_size=14, color=YELLOW)
        stage2_label.next_to(tokens_group, DOWN, buff=0.3)
        self.play(Write(stage2_label))
        self.wait(1)

        # Arrow 2
        arrow2 = Arrow(tokens_group.get_bottom() + DOWN * 0.5, LEFT * 3 + DOWN * 2.5, buff=0.1, color=WHITE)
        self.play(Create(arrow2))

        # Stage 3: Postfix
        postfix_box = Rectangle(width=3, height=0.6, color=BLUE)
        postfix_text = Text("[2, 3, 4, *, +]", font_size=14, color=WHITE)
        postfix_group = VGroup(postfix_box, postfix_text)
        postfix_group.shift(LEFT * 3 + DOWN * 2.5)

        self.play(Create(postfix_box), Write(postfix_text))
        stage3_label = Text("Shunting Yard", font_size=14, color=YELLOW)
        stage3_label.next_to(postfix_group, DOWN, buff=0.3)
        self.play(Write(stage3_label))
        self.wait(1)

        # Arrow 3 to tree
        arrow3 = Arrow(postfix_group.get_right() + RIGHT * 0.5, RIGHT * 3 + DOWN * 0.5, buff=0.1, color=WHITE)
        self.play(Create(arrow3))

        # Stage 4: Tree
        tree_root = TreeNode("+", "operator")
        tree_root.shift(RIGHT * 3 + UP * 1.5)

        tree_left = TreeNode("2", "operand")
        tree_left.shift(RIGHT * 1 + DOWN * 0.5)

        tree_right = TreeNode("*", "operator")
        tree_right.shift(RIGHT * 5 + DOWN * 0.5)

        tree_ll = TreeNode("3", "operand")
        tree_ll.shift(RIGHT * 3.5 + DOWN * 2)

        tree_lr = TreeNode("4", "operand")
        tree_lr.shift(RIGHT * 6.5 + DOWN * 2)

        self.play(Create(tree_root), Create(tree_left), Create(tree_right), Create(tree_ll), Create(tree_lr))

        tree_edges = [
            Line(tree_root.get_center(), tree_left.get_center(), color=BLUE),
            Line(tree_root.get_center(), tree_right.get_center(), color=BLUE),
            Line(tree_right.get_center(), tree_ll.get_center(), color=BLUE),
            Line(tree_right.get_center(), tree_lr.get_center(), color=BLUE),
        ]

        for edge in tree_edges:
            self.play(Create(edge), run_time=0.3)

        stage4_label = Text("Build Tree", font_size=14, color=YELLOW)
        stage4_label.shift(RIGHT * 3)
        self.play(Write(stage4_label))
        self.wait(1)

        # Result
        result = Text("Result: 14", font_size=32, color=GREEN)
        result.shift(DOWN * 3.5)
        self.play(Write(result))

        self.wait(2)


if __name__ == "__main__":
    pass

