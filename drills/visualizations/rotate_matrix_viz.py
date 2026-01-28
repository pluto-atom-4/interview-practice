from __future__ import annotations

from manim import (
    BLUE,
    DOWN,
    GREEN,
    LEFT,
    ORIGIN,
    RED,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Arrow,
    Create,
    FadeIn,
    FadeOut,
    Indicate,
    Rectangle,
    Scene,
    Text,
    VGroup,
    Write,
)


class MatrixRotationVisualization(Scene):
    """
    Visualization of the 90-degree clockwise matrix rotation algorithm.

    Shows the step-by-step transformation using the coordinate transformation formula:
    rotated[c][rows - 1 - r] = matrix[r][c]

    Uses a 3×3 matrix example:
    Original: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    Rotated:  [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

    Visualizes:
    1. Original matrix on the left
    2. Empty rotated matrix (with swapped dimensions) on the right
    3. Element-by-element transformation with arrows showing coordinate mapping
    4. Color-coded elements to track movement through the algorithm
    5. Transformation formula displayed during animation
    """

    def construct(self):
        # Original matrix
        original_matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ]

        rows, cols = len(original_matrix), len(original_matrix[0])

        # Title
        title = Text("Matrix Rotation: 90° Clockwise", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Subtitle with formula
        formula = Text(
            "Formula: rotated[c][rows - 1 - r] = matrix[r][c]",
            font_size=20,
            color=YELLOW,
        ).next_to(title, DOWN, buff=0.3)
        self.play(Write(formula))
        self.wait(0.5)

        # Original matrix label and visualization
        original_label = Text("Original Matrix (3×3):", font_size=22, color=BLUE).to_edge(
            LEFT
        ).shift(UP * 2)
        self.play(Write(original_label))

        # Create original matrix boxes
        original_boxes = VGroup()
        original_texts = VGroup()
        for r in range(rows):
            for c in range(cols):
                box = Rectangle(width=0.6, height=0.6, color=BLUE, stroke_width=2)
                text = Text(
                    str(original_matrix[r][c]), font_size=18, color=WHITE
                ).move_to(box.get_center())
                box_group = VGroup(box, text).move_to(
                    ORIGIN + LEFT * 3 + DOWN * 0.5 + RIGHT * (c * 0.8) + DOWN * (r * 0.8)
                )
                original_boxes.add(box)
                original_texts.add(text)

        self.play(Create(original_boxes))
        self.play(Create(original_texts))
        self.wait(1)

        # Rotated matrix label
        rotated_label = Text("Rotated Matrix (3×3):", font_size=22, color=GREEN).to_edge(
            RIGHT
        ).shift(UP * 2)
        self.play(Write(rotated_label))

        # Create rotated matrix boxes (empty initially)
        rotated_boxes = VGroup()
        rotated_texts = VGroup()
        for r in range(cols):  # Dimensions swapped
            for c in range(rows):
                box = Rectangle(width=0.6, height=0.6, color=GREEN, stroke_width=2)
                text = Text("", font_size=18, color=WHITE).move_to(box.get_center())
                box_group = VGroup(box, text).move_to(
                    ORIGIN + RIGHT * 3 + DOWN * 0.5 + RIGHT * (c * 0.8) + DOWN * (r * 0.8)
                )
                rotated_boxes.add(box)
                rotated_texts.add(text)

        self.play(Create(rotated_boxes))
        self.wait(0.5)

        # Color palette for tracking elements
        colors = [RED, YELLOW, BLUE, GREEN, BLUE, RED, YELLOW, BLUE, GREEN]

        # Animate transformation element by element
        for r in range(rows):
            for c in range(cols):
                # Calculate new position
                new_r = c
                new_c = rows - 1 - r
                element_value = original_matrix[r][c]

                # Get indices in flattened arrays
                original_idx = r * cols + c
                rotated_idx = new_r * rows + new_c

                # Highlight source element
                source_box = original_boxes[original_idx]
                source_text = original_texts[original_idx]
                self.play(
                    Indicate(source_box, color=colors[original_idx], scale_factor=1.2)
                )

                # Update transformation formula display with current indices
                current_formula = Text(
                    f"matrix[{r}][{c}] → rotated[{new_r}][{new_c}] = {element_value}",
                    font_size=18,
                    color=colors[original_idx],
                ).next_to(formula, DOWN, buff=0.5)
                self.play(Write(current_formula))

                # Draw arrow from source to destination
                source_center = source_box.get_center()
                dest_center = rotated_boxes[rotated_idx].get_center()
                arrow = Arrow(
                    source_center,
                    dest_center,
                    color=colors[original_idx],
                    stroke_width=2,
                    buff=0.1,
                )
                self.play(Create(arrow))

                # Update destination text
                rotated_texts[rotated_idx].set_text(str(element_value))
                self.play(
                    FadeIn(rotated_texts[rotated_idx]),
                    Indicate(rotated_boxes[rotated_idx], color=colors[original_idx]),
                )

                # Fade out current formula and arrow
                self.play(FadeOut(current_formula), FadeOut(arrow))
                self.wait(0.3)

        # Final result summary
        self.wait(0.5)
        result_label = Text("Transformation Complete!", font_size=24, color=GREEN).to_edge(
            DOWN
        )
        self.play(Write(result_label))
        self.wait(1)

        # Summary box
        summary = Text(
            "Time: O(n×m) | Space: O(n×m) | Non-mutating",
            font_size=18,
            color=WHITE,
        ).next_to(result_label, DOWN, buff=0.3)
        self.play(Write(summary))
        self.wait(2)
