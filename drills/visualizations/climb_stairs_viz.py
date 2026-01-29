"""
## Operation Overview

Visualization of the space-optimized dynamic programming solution to the Climb Stairs problem.

Shows the step-by-step computation using the Fibonacci recurrence relation:
ways[n] = ways[n-1] + ways[n-2]

Example with n=5:
- Base cases: ways(1)=1, ways(2)=2
- Iteration: ways(3)=3, ways(4)=5, ways(5)=8
- Result: 8 distinct ways to climb 5 stairs

Visualizes:
1. Stair structure on the left (visual reference for n)
2. Rolling window with prev2 and prev1 variables
3. Step-by-step computation loop from stair 3 to n
4. Current value calculation (prev1 + prev2)
5. Variable sliding/window update after each iteration
"""

from manim import (
    BLACK,
    BLUE,
    DOWN,
    GREEN,
    LEFT,
    ORANGE,
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


class ClimbStairsVisualization(Scene):
    """
    Visualization of the space-optimized dynamic programming solution for Climb Stairs.

    Shows how the algorithm maintains only two rolling window variables (prev2, prev1)
    to compute the number of ways to reach each stair using the recurrence relation:
    current = prev1 + prev2.

    Animation sequences through stairs 1-5, highlighting how prev2 and prev1 slide
    through the computation, with color-coded boxes and arrows showing the addition
    and state transitions.
    """

    def construct(self):
        # Title and formula
        title = Text("Climb Stairs: Space-Optimized DP", font_size=40)
        title.to_edge(UP)
        self.play(Write(title))

        formula = Text("Recurrence: ways[n] = ways[n-1] + ways[n-2]", font_size=24)
        formula.next_to(title, DOWN, buff=0.3)
        self.play(Write(formula))
        self.wait(1)

        # Scene layout: stairs on left, rolling window on right
        stairs_group = self._create_stairs(n=5)
        stairs_group.next_to(title, DOWN, buff=1.5)
        stairs_group.to_edge(LEFT, buff=0.5)

        self.play(Create(stairs_group))
        self.wait(0.5)

        # Right side: rolling window visualization
        window_label = Text("Rolling Window (Two Variables)", font_size=20)
        window_label.to_edge(RIGHT, buff=0.5)
        window_label.move_to([5, 3, 0])
        self.play(Write(window_label))

        # Animation loop for stairs 3-5
        self._animate_rolling_window(stairs_group, start_stair=3, end_stair=5)

        # Summary
        self.wait(1)
        summary = Text(
            "Time: O(n)  |  Space: O(1)  |  Only two variables needed!",
            font_size=18,
            color=GREEN,
        )
        summary.to_edge(DOWN)
        self.play(Write(summary))
        self.wait(2)

    def _create_stairs(self, n):
        """Create visual representation of n stairs with step numbers."""
        stairs = VGroup()
        step_height = 0.5
        step_width = 0.6

        for i in range(1, n + 1):
            # Stair box
            stair = Rectangle(
                width=step_width, height=step_height, color=BLUE, stroke_width=2
            )
            x_pos = (i - 1) * (step_width + 0.1)
            y_pos = (i - 1) * step_height
            stair.move_to([x_pos, y_pos, 0])

            # Label with step number
            label = Text(str(i), font_size=16, color=WHITE)
            label.move_to(stair.get_center())

            stairs.add(stair, label)

        # Group label
        stairs_label = Text("n stairs →", font_size=14)
        stairs_label.next_to(stairs, LEFT, buff=0.2)
        stairs.add(stairs_label)

        return stairs

    def _animate_rolling_window(self, stairs_group, start_stair=3, end_stair=5):
        """Animate the rolling window computation for stairs start_stair to end_stair."""
        base_y = -1.5
        rolling_y = base_y

        # Initialize base cases
        prev2_val, prev1_val = 1, 2
        prev2_box = None
        prev1_box = None
        current_box = None

        for stair in range(start_stair, end_stair + 1):
            self.wait(0.5)

            # Clear previous window
            if stair > start_stair and prev2_box is not None and prev1_box is not None:
                self.play(FadeOut(prev2_box), FadeOut(prev1_box), FadeOut(current_box))

            # Create current iteration window
            prev2_box = self._create_value_box(
                "prev2", prev2_val, color=RED, y_pos=rolling_y - 1
            )
            prev1_box = self._create_value_box(
                "prev1", prev1_val, color=ORANGE, y_pos=rolling_y
            )

            self.play(FadeIn(prev2_box), FadeIn(prev1_box))
            self.wait(0.3)

            # Addition animation
            current_val = prev1_val + prev2_val
            add_text = Text(f"{prev1_val} + {prev2_val} = {current_val}", font_size=20)
            add_text.move_to([5, rolling_y + 1.2, 0])
            self.play(Write(add_text))
            self.wait(0.5)

            # Create current value box
            current_box = self._create_value_box(
                f"ways[{stair}]", current_val, color=GREEN, y_pos=rolling_y + 1.2
            )
            self.play(FadeIn(current_box))
            self.wait(0.3)

            # Highlight the stair on the left
            stair_index = stair - 1
            stair_boxes = [
                child
                for child in stairs_group.submobjects
                if isinstance(child, Rectangle)
            ]
            if stair_index < len(stair_boxes):
                self.play(Indicate(stair_boxes[stair_index], color=GREEN, scale_factor=1.3))

            self.wait(0.3)

            # Update for next iteration
            prev2_val = prev1_val
            prev1_val = current_val

            self.play(FadeOut(add_text))

        # Final result display and cleanup
        self.wait(0.5)
        if prev2_box is not None and prev1_box is not None and current_box is not None:
            self.play(FadeOut(prev2_box), FadeOut(prev1_box), FadeOut(current_box))

        result_text = Text(f"Result: climb_stairs(5) = {prev1_val}", font_size=24, color=GREEN)
        result_text.move_to([5, rolling_y + 2.5, 0])
        self.play(Write(result_text))

    def _create_value_box(self, label, value, color, y_pos):
        """Create a labeled value box for display."""
        box = Rectangle(width=1.2, height=0.6, color=color, stroke_width=2)
        box.move_to([5, y_pos, 0])

        label_text = Text(label, font_size=14)
        label_text.move_to([3.5, y_pos, 0])

        value_text = Text(str(value), font_size=18, color=color)
        value_text.move_to(box.get_center())

        return VGroup(label_text, box, value_text)
