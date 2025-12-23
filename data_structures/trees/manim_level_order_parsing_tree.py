"""
Manim Animation for Level-Order Parsing Tree
==============================================

Demonstrates the motion of parsing trees using Manim animations.
Shows step-by-step:
1. Tokenization process
2. Shunting Yard algorithm
3. Tree construction
4. Level-order traversal
5. Expression evaluation

Usage:
    manim -pql manim_level_order_parsing_tree.py TokenizationAnimation
    manim -pql manim_level_order_parsing_tree.py ShuntingYardAnimation
    manim -pql manim_level_order_parsing_tree.py TreeConstructionAnimation
    manim -pql manim_level_order_parsing_tree.py LevelOrderTraversalAnimation
    manim -pql manim_level_order_parsing_tree.py ExpressionEvaluationAnimation
"""

from typing import List, Tuple

from manim import *


class TokenizationAnimation(Scene):
    """Animate the tokenization process of a mathematical expression."""

    def construct(self):
        # Title
        title = Text("Step 1: Tokenization", font_size=40, color=BLUE).to_edge(UP)
        self.add(title)

        # Original expression
        expression = "2 + 3 * 4"
        expr_text = Text(expression, font_size=36, color=WHITE).shift(UP * 2)
        self.play(Write(expr_text))
        self.wait(1)

        # Explanation
        explanation = Text("Breaking expression into tokens", font_size=24, color=YELLOW)
        explanation.next_to(expr_text, DOWN, buff=0.5)
        self.play(Write(explanation))
        self.wait(1)

        # Show tokens appearing
        tokens = ["2", "+", "3", "*", "4"]
        token_objects = []

        for i, token in enumerate(tokens):
            token_box = Rectangle(height=0.8, width=0.8, color=GREEN)
            token_text = Text(token, font_size=32, color=WHITE)
            token_group = VGroup(token_box, token_text)
            token_group.arrange(DOWN)
            token_group.shift(LEFT * 4 + i * 1.8 + DOWN * 1.5)

            token_objects.append(token_group)
            self.play(Create(token_box), Write(token_text), run_time=0.5)

        self.wait(1)

        # Arrow from expression to tokens
        arrow = Arrow(expr_text.get_bottom(), token_objects[0].get_top() + UP * 0.3, buff=0.1)
        self.play(Create(arrow))

        # Highlight each token
        for token_group in token_objects:
            self.play(token_group.animate.set_color(YELLOW), run_time=0.3)
            self.play(token_group.animate.set_color(GREEN), run_time=0.3)

        self.wait(2)

        # Show result
        result = Text(f"Result: {tokens}", font_size=24, color=BLUE)
        result.next_to(token_objects[-1], DOWN, buff=1)
        self.play(Write(result))

        self.wait(2)


class ShuntingYardAnimation(Scene):
    """Animate the Shunting Yard algorithm (Infix to Postfix)."""

    def construct(self):
        # Title
        title = Text("Step 2: Shunting Yard Algorithm", font_size=40, color=BLUE).to_edge(UP)
        self.add(title)

        # Initial state
        expression = "2 + 3 * 4"
        tokens = ["2", "+", "3", "*", "4"]

        expr_text = Text(f"Infix: {expression}", font_size=32, color=WHITE)
        expr_text.shift(UP * 1.5)
        self.play(Write(expr_text))

        # Create stack and output areas
        stack_label = Text("Operator Stack:", font_size=24, color=YELLOW)
        stack_label.shift(LEFT * 4 + DOWN * 0.5)
        self.play(Write(stack_label))

        output_label = Text("Output:", font_size=24, color=BLUE)
        output_label.shift(RIGHT * 4 + DOWN * 0.5)
        self.play(Write(output_label))

        # Stack and output display
        stack_display = Text("", font_size=20, color=YELLOW)
        stack_display.next_to(stack_label, DOWN, buff=0.3).align_to(stack_label, LEFT)

        output_display = Text("", font_size=20, color=BLUE)
        output_display.next_to(output_label, DOWN, buff=0.3).align_to(output_label, LEFT)

        self.add(stack_display, output_display)

        # Simulate Shunting Yard
        stack = []
        output = []
        step_count = 1

        for token in tokens:
            # Step label
            step_text = Text(f"Token: {token}", font_size=20, color=GREEN)
            step_text.shift(UP * 0.3)

            if token not in "+-*/()^":
                output.append(token)
            elif token in "+-*/":
                stack.append(token)

            # Update displays
            stack_str = " ".join(stack) if stack else "empty"
            output_str = " ".join(output) if output else "empty"

            new_stack_display = Text(stack_str, font_size=20, color=YELLOW)
            new_stack_display.next_to(stack_label, DOWN, buff=0.3).align_to(stack_label, LEFT)

            new_output_display = Text(output_str, font_size=20, color=BLUE)
            new_output_display.next_to(output_label, DOWN, buff=0.3).align_to(output_label, LEFT)

            self.play(Write(step_text), run_time=0.5)
            self.play(Transform(stack_display, new_stack_display), Transform(output_display, new_output_display), run_time=0.5)
            self.wait(0.5)

            step_count += 1

        self.wait(1)

        # Final result
        result_text = Text(f"Postfix: {' '.join(output)}", font_size=32, color=BLUE)
        result_text.shift(DOWN * 2.5)
        self.play(Write(result_text))

        self.wait(2)


class TreeConstructionAnimation(Scene):
    """Animate the tree construction from postfix notation."""

    def construct(self):
        # Title
        title = Text("Step 3: Tree Construction", font_size=40, color=BLUE).to_edge(UP)
        self.add(title)

        # Expression info
        info = Text("Building tree from postfix: 2 3 4 * +", font_size=24, color=YELLOW)
        info.shift(UP * 2)
        self.play(Write(info))

        # Stack area
        stack_label = Text("Stack State:", font_size=24, color=GREEN)
        stack_label.shift(LEFT * 4 + UP * 0.5)
        self.play(Write(stack_label))

        # Center area for tree construction
        tree_center = np.array([0, 0, 0])

        # Simulate postfix stack building
        postfix = ["2", "3", "4", "*", "+"]
        nodes = {}
        node_counter = 0

        for i, token in enumerate(postfix):
            step_text = Text(f"Processing: {token}", font_size=20, color=BLUE)
            step_text.shift(UP * 0.5)

            if token not in "+-*/":
                # Create operand node
                operand_circle = Circle(radius=0.3, color=GREEN, fill_opacity=0.7)
                operand_text = Text(token, font_size=18, color=WHITE)
                operand_group = VGroup(operand_circle, operand_text)
                operand_group.move_to(tree_center + DOWN * (i * 0.5))

                nodes[node_counter] = operand_group
                node_counter += 1

                self.play(Write(step_text), run_time=0.3)
                self.play(Create(operand_circle), Write(operand_text), run_time=0.5)
            else:
                # Create operator node
                operator_circle = Circle(radius=0.3, color=RED, fill_opacity=0.7)
                operator_text = Text(token, font_size=18, color=WHITE)
                operator_group = VGroup(operator_circle, operator_text)
                operator_group.move_to(tree_center)

                self.play(Write(step_text), run_time=0.3)
                self.play(Create(operator_circle), Write(operator_text), run_time=0.5)

            self.wait(0.5)

        self.wait(2)


class LevelOrderTraversalAnimation(Scene):
    """Animate level-order traversal of an expression tree."""

    def construct(self):
        # Title
        title = Text("Step 4: Level-Order Traversal (BFS)", font_size=40, color=BLUE).to_edge(UP)
        self.add(title)

        # Create a sample expression tree visualization
        tree_info = Text("Expression: 2 + 3 * 4", font_size=24, color=YELLOW)
        tree_info.shift(UP * 2)
        self.play(Write(tree_info))

        # Create tree nodes
        # Root
        root_circle = Circle(radius=0.4, color=RED, fill_opacity=0.7)
        root_text = Text("+", font_size=20, color=WHITE)
        root_text.move_to(root_circle.get_center())
        root = VGroup(root_circle, root_text).shift(UP * 1)

        # Level 1
        left_circle = Circle(radius=0.4, color=GREEN, fill_opacity=0.7)
        left_text = Text("2", font_size=20, color=WHITE)
        left_text.move_to(left_circle.get_center())
        left_node = VGroup(left_circle, left_text).shift(LEFT * 2 + DOWN * 0.5)

        right_circle = Circle(radius=0.4, color=RED, fill_opacity=0.7)
        right_text = Text("*", font_size=20, color=WHITE)
        right_text.move_to(right_circle.get_center())
        right_node = VGroup(right_circle, right_text).shift(RIGHT * 2 + DOWN * 0.5)

        # Level 2
        left_left_circle = Circle(radius=0.4, color=GREEN, fill_opacity=0.7)
        left_left_text = Text("3", font_size=20, color=WHITE)
        left_left_text.move_to(left_left_circle.get_center())
        left_left = VGroup(
            left_left_circle,
            left_left_text
        ).shift(LEFT * 3.5 + DOWN * 2)

        left_right_circle = Circle(radius=0.4, color=GREEN, fill_opacity=0.7)
        left_right_text = Text("4", font_size=20, color=WHITE)
        left_right_text.move_to(left_right_circle.get_center())
        left_right = VGroup(
            left_right_circle,
            left_right_text
        ).shift(RIGHT * 0.5 + DOWN * 2)

        # Draw tree
        self.play(Create(root_circle), Write(root_text))
        self.play(Create(left_circle), Write(left_text))
        self.play(Create(right_circle), Write(right_text))
        self.play(Create(left_left[0]), Write(left_left[1]))
        self.play(Create(left_right[0]), Write(left_right[1]))

        # Draw edges
        line1 = Line(root.get_center(), left_node.get_center(), color=BLUE)
        line2 = Line(root.get_center(), right_node.get_center(), color=BLUE)
        line3 = Line(right_node.get_center(), left_left.get_center(), color=BLUE)
        line4 = Line(right_node.get_center(), left_right.get_center(), color=BLUE)

        self.play(Create(line1), Create(line2), Create(line3), Create(line4))
        self.wait(1)

        # Traverse level by level
        level_text = Text("Level 0:", font_size=20, color=YELLOW)
        level_text.shift(DOWN * 3.5)
        self.play(Write(level_text))
        self.play(root_circle.animate.set_color(YELLOW))
        self.wait(0.5)

        level_text_1 = Text("Level 1:", font_size=20, color=YELLOW)
        level_text_1.shift(DOWN * 3.5)
        self.play(Transform(level_text, level_text_1))
        self.play(left_circle.animate.set_color(YELLOW), right_circle.animate.set_color(YELLOW))
        self.wait(0.5)

        level_text_2 = Text("Level 2:", font_size=20, color=YELLOW)
        level_text_2.shift(DOWN * 3.5)
        self.play(Transform(level_text, level_text_2))
        self.play(left_left[0].animate.set_color(YELLOW), left_right[0].animate.set_color(YELLOW))
        self.wait(0.5)

        # Show traversal order
        result = Text("Traversal Order: + → 2 → * → 3 → 4", font_size=24, color=BLUE)
        result.shift(DOWN * 4.5)
        self.play(Write(result))

        self.wait(2)


class ExpressionEvaluationAnimation(Scene):
    """Animate the expression evaluation process."""

    def construct(self):
        # Title
        title = Text("Step 5: Expression Evaluation", font_size=40, color=BLUE).to_edge(UP)
        self.add(title)

        # Expression
        expression = Text("Evaluate: 2 + 3 * 4", font_size=32, color=YELLOW)
        expression.shift(UP * 2)
        self.play(Write(expression))

        # Evaluation steps
        steps = [
            "Step 1: Identify operations: 3 * 4",
            "Step 2: Calculate: 3 * 4 = 12",
            "Step 3: Calculate: 2 + 12 = 14",
            "Result: 14"
        ]

        y_pos = 1
        for step in steps:
            step_text = Text(step, font_size=20, color=BLUE)
            step_text.shift(UP * y_pos)
            self.play(Write(step_text), run_time=0.8)
            self.wait(0.5)
            y_pos -= 0.6

        # Final result
        result = Text("Final Result: 14", font_size=40, color=GREEN)
        result.shift(DOWN * 2.5)
        self.play(Write(result), run_time=1)

        self.wait(2)


class CompleteParsingSummary(Scene):
    """Show complete parsing process summary with all steps."""

    def construct(self):
        # Title
        title = Text("Complete Parsing Process Summary", font_size=44, color=BLUE)
        title.to_edge(UP)
        self.add(title)

        # Create sections for each step
        sections = [
            ("1. Tokenization", "2 + 3 * 4 → [2, +, 3, *, 4]", GREEN),
            ("2. Shunting Yard", "[2, +, 3, *, 4] → [2, 3, 4, *, +]", YELLOW),
            ("3. Tree Build", "Stack → Binary Tree", RED),
            ("4. Traversal", "Level-order: → 2 → * → 3 → 4", BLUE),
            ("5. Evaluation", "Result = 14", CYAN),
        ]

        y_position = 2.5
        for i, (step, description, color) in enumerate(sections):
            # Step title
            step_title = Text(step, font_size=24, color=color, weight=BOLD)
            step_title.shift(UP * y_position)

            # Description
            desc_text = Text(description, font_size=18, color=WHITE)
            desc_text.next_to(step_title, RIGHT, buff=0.5)

            # Number circle
            number_circle = Circle(radius=0.25, color=color, fill_opacity=0.7)
            number_text = Text(str(i + 1), font_size=16, color=WHITE)
            number_group = VGroup(number_circle, number_text)
            number_group.next_to(step_title, LEFT, buff=0.5)

            self.play(Create(number_circle), Write(number_text), run_time=0.3)
            self.play(Write(step_title), Write(desc_text), run_time=0.5)

            # Arrow to next
            if i < len(sections) - 1:
                arrow = Arrow(DOWN * 0.2, DOWN * -0.3, buff=0.05, color=WHITE)
                arrow.next_to(step_title, DOWN, buff=0.3)
                self.play(Create(arrow), run_time=0.3)

            y_position -= 1.0
            self.wait(0.5)

        self.wait(2)


class InteractiveExpressionParser(Scene):
    """Interactive scene showing multiple expressions being parsed."""

    def construct(self):
        # Title
        title = Text("Multiple Expression Examples", font_size=40, color=BLUE)
        title.to_edge(UP)
        self.add(title)

        expressions = [
            ("2 + 3", "5"),
            ("2 * 3 + 4", "10"),
            ("(2 + 3) * 4", "20"),
        ]

        y_pos = 1.5
        for expr, result in expressions:
            # Expression
            expr_text = Text(f"{expr} =", font_size=24, color=YELLOW)
            expr_text.shift(UP * y_pos)
            self.play(Write(expr_text), run_time=0.5)

            # Result (hidden first)
            result_text = Text(result, font_size=24, color=GREEN)
            result_text.next_to(expr_text, RIGHT, buff=0.5)

            # Animate result appearance
            self.wait(0.5)
            self.play(Write(result_text), run_time=0.8)
            self.wait(0.5)

            y_pos -= 0.8

        self.wait(2)


if __name__ == "__main__":
    # Note: Run individual scenes with:
    # manim -pql manim_level_order_parsing_tree.py TokenizationAnimation
    # manim -pql manim_level_order_parsing_tree.py ShuntingYardAnimation
    # etc.
    pass

