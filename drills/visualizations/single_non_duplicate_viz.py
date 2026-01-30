"""
## Operation Overview

Visualization of the XOR bitwise operation finding a single non-duplicate number.

Shows the step-by-step XOR cancellation process where identical numbers cancel out 
(become 0) and the single unpaired number survives unchanged.

Example with concrete values:
Input: [4, 2, 7, 2, 4]
Expected: 7

Visualizes:
1. Input array with paired elements (colored) and single element (highlighted)
2. Step-by-step XOR operations combining array elements
3. How pairs cancel to 0 while single number passes through unchanged
4. XOR formula: result ^= num (with current indices)
5. Final result showing only the unpaired number remaining
"""

from manim import (
    BLUE,
    DOWN,
    GRAY,
    GREEN,
    LEFT,
    ORANGE,
    ORIGIN,
    PURPLE,
    RED,
    RIGHT,
    TEAL,
    UP,
    WHITE,
    YELLOW,
)
from manim import (
    Arrow as ManimArrow,  # Colors; Directions; Shapes; Animations; Text and rendering
)
from manim import (
    Create,
    FadeIn,
    FadeOut,
    Indicate,
    Line,
    Rectangle,
    Scene,
    Text,
    Transform,
    VGroup,
    Write,
)


class SingleNonDuplicateVisualization(Scene):
    """
    Visualization of finding the single non-duplicate using XOR bitwise operations.

    The algorithm XORs all elements together. Because XOR has the properties:
    - x ^ x = 0 (same values cancel)
    - x ^ 0 = x (identity)
    - Commutativity and associativity

    Duplicate pairs cancel out, leaving only the single number visible at the end.
    """

    def construct(self):
        # ===== Scene Layout Strategy =====
        # - Title at top
        # - Input array on left side (elements with colors for pairs)
        # - XOR operation trace in center (shows each step)
        # - Result tracking on right side (accumulating XOR)
        # - Formula display below operations

        # ===== Color Scheme =====
        # - BLUE, RED, GREEN, YELLOW: Paired elements (same color for pair)
        # - ORANGE: Single non-duplicate element
        # - WHITE: Labels and text
        # - GRAY: Neutral/background

        # ===== Example Data =====
        nums = [4, 2, 7, 2, 4]
        color_map = {4: BLUE, 2: RED, 7: ORANGE}  # 7 is single, others are paired
        single_num = 7

        # ===== Title and Header =====
        title = Text("Finding Single Non-Duplicate with XOR", font_size=24, color=WHITE)
        title.move_to(ORIGIN + UP * 3.5)
        self.play(Write(title))
        self.wait(0.3)

        # ===== Build Input Array Display =====
        # Position calculation: array from left side
        array_start_x = -3.2
        element_width = 0.7
        array_y = 2.2

        array_elements = VGroup()
        element_boxes = []

        for i, num in enumerate(nums):
            box = Rectangle(width=0.6, height=0.6, color=color_map[num], stroke_width=2)
            num_text = Text(str(num), font_size=16, color=WHITE)

            pos_x = array_start_x + i * element_width
            box.move_to(ORIGIN + RIGHT * pos_x + UP * array_y)
            num_text.move_to(box.get_center())

            array_elements.add(box, num_text)
            element_boxes.append((box, num_text, num))

        # Label for input array
        input_label = Text("Input:", font_size=12, color=GRAY)
        input_label.move_to(ORIGIN + LEFT * 3.8 + UP * array_y)

        self.play(Create(input_label), Create(array_elements))
        self.wait(0.5)

        # ===== Build Result Tracking Area =====
        # Shows accumulating XOR result on the right side
        result_label = Text("result = 0", font_size=12, color=WHITE)
        result_label.move_to(ORIGIN + RIGHT * 2.5 + UP * 2.2)
        self.play(Write(result_label))

        # ===== Animation Flow =====
        # Step through each element, showing XOR operation
        result = 0
        result_text_obj = result_label

        for step, (box, num_text, num) in enumerate(element_boxes):
            # Highlight current element
            self.play(Indicate(box, color=WHITE, scale_factor=1.4))

            # Show operation formula
            formula = Text(f"result = {result} ⊕ {num}", font_size=14, color=YELLOW)
            formula.move_to(ORIGIN + UP * 1.2)
            self.play(Write(formula))
            self.wait(0.4)

            # Calculate new result
            old_result = result
            result ^= num
            new_result_display = f"result = {result}"

            if result == 0:
                new_result_text = Text(new_result_display + " (pair canceled!)", font_size=12, color=GREEN)
            else:
                new_result_text = Text(new_result_display, font_size=12, color=WHITE)

            new_result_text.move_to(ORIGIN + RIGHT * 2.5 + UP * 2.2)

            # Animate result update
            self.play(
                FadeOut(result_text_obj),
                FadeIn(new_result_text),
                FadeOut(formula),
            )
            result_text_obj = new_result_text
            self.wait(0.3)

        # ===== Final Summary Section =====
        self.wait(0.5)

        # Display final result with emphasis
        summary_line = Text(
            f"Final: result = {single_num}",
            font_size=16,
            color=ORANGE,
        )
        summary_line.move_to(ORIGIN + DOWN * 0.8)
        self.play(Write(summary_line))

        # Explanation text
        explanation = Text(
            "All pairs canceled (x ⊕ x = 0),\nonly the single number survived (x ⊕ 0 = x)",
            font_size=12,
            color=GRAY,
        )
        explanation.move_to(ORIGIN + DOWN * 1.8)
        self.play(Write(explanation))

        # Complexity info
        complexity = Text("Time: O(n)  Space: O(1)", font_size=11, color=GRAY)
        complexity.move_to(ORIGIN + DOWN * 2.5)
        self.play(Write(complexity))

        self.wait(1)

        # ===== Key Visualization Concepts =====
        """
        - Why color-code paired elements?
        Pairs use the same color to make the duplicate relationship immediately visible.
        The single element in a different color (orange) stands out, helping viewers see
        which number survives the XOR cancellation.

        - Why show each XOR step individually?
        Step-by-step animation makes the cancellation property clear. Viewers see how
        each operation either cancels a pair (result becomes 0) or passes through an
        unpaired element, reinforcing the mathematical intuition.

        - Why display the formula during each step?
        The formula shows current values (old result, current number) and result,
        making the bitwise operation concrete rather than abstract. Real indices keep
        the example grounded in the actual algorithm.
        """

        """
        Animation Sequence:
        1. Title display (0.3s write + 0.5s wait)
        2. Input array creation with colors (0.5s wait)
        3. Initialize result label (right side)
        4. For each element:
           a. Highlight current element (Indicate with scale)
           b. Display formula with current values (Write)
           c. Perform XOR operation and update result (0.4s formula + display)
           d. Show new result (FadeOut old, FadeIn new)
           e. Wait 0.3s before next step
        5. Final summary with explanation (complexity info)
        6. Total animation: ~15-20 seconds for 5-element array
        """


class SingleNonDuplicateVisualizationExtended(Scene):
    """
    Extended visualization showing XOR properties in detail.

    Demonstrates:
    1. Why x ^ x = 0 (pair cancellation)
    2. Why x ^ 0 = x (identity property)
    3. Complete algorithm flow with multiple examples
    """

    def construct(self):
        # ===== Title =====
        title = Text("XOR Properties: Finding Single Non-Duplicate", font_size=20, color=WHITE)
        title.move_to(ORIGIN + UP * 3.5)
        self.play(Write(title))
        self.wait(0.3)

        # ===== Property 1: x ^ x = 0 =====
        prop1_label = Text("Property 1: x ⊕ x = 0", font_size=14, color=BLUE)
        prop1_label.move_to(ORIGIN + UP * 2.5)
        self.play(Write(prop1_label))

        # Show example: 4 ^ 4 = 0
        example1 = Text("4 ⊕ 4 = 0", font_size=16, color=YELLOW)
        example1.move_to(ORIGIN + UP * 1.8)
        self.play(Write(example1))
        self.wait(0.5)

        # ===== Property 2: x ^ 0 = x =====
        prop2_label = Text("Property 2: x ⊕ 0 = x (identity)", font_size=14, color=RED)
        prop2_label.move_to(ORIGIN + UP * 0.8)
        self.play(Write(prop2_label))

        example2 = Text("7 ⊕ 0 = 7", font_size=16, color=YELLOW)
        example2.move_to(ORIGIN + UP * 0.1)
        self.play(Write(example2))
        self.wait(0.5)

        # ===== Algorithm Conclusion =====
        conclusion_label = Text("Algorithm: XOR all elements", font_size=14, color=GREEN)
        conclusion_label.move_to(ORIGIN + DOWN * 1.0)
        self.play(Write(conclusion_label))

        algo_steps = Text(
            "1. Initialize result = 0\n"
            "2. For each number: result ⊕= number\n"
            "3. Pairs become 0, single number survives\n"
            "4. Return result",
            font_size=11,
            color=WHITE,
        )
        algo_steps.move_to(ORIGIN + DOWN * 2.2)
        self.play(Write(algo_steps))

        self.wait(1)


"""
## Implementation Notes

Technical Implementation Decisions:

1. Color Mapping Strategy:
   - Map each value (4, 2, 7) to a distinct color
   - Use ORANGE for the single non-duplicate element
   - Consistent coloring throughout animation maintains visual tracking
   - Color persistence helps viewers associate elements across steps

2. Position Calculation:
   - Input array: array_start_x = -3.2, element_width = 0.7
   - Each element positioned at: array_start_x + index * element_width
   - Y position: array_y = 2.2 (upper portion of screen)
   - Result display: right side at (RIGHT * 2.5, UP * 2.2)
   - Layout utilizes screen space with left array, center operations, right result

3. Animation Timing:
   - Per-element animation: ~1.2 seconds (0.4s formula + 0.3s updates + waits)
   - Total for N elements: ~1.2*N seconds
   - Timing allows viewers to follow each operation without feeling rushed

4. XOR Operation Visualization:
   - Each step shows: highlight element → formula display → result update
   - Result transitions smoothly (FadeOut old, FadeIn new)
   - Green text highlights pair cancellations (result = 0)
   - White text for identity preservation (single number passes through)

5. Summary Display:
   - Final result emphasized in ORANGE (matches single element color)
   - Multi-line explanation reinforces the two key XOR properties
   - Complexity info provides technical context

## Summary Formats

**30-Second Pitch:**
"This animation demonstrates how the XOR bitwise operation elegantly finds a single
non-duplicate number in an array. By XORing all elements together, duplicate pairs
cancel out (because x ⊕ x = 0) while the single number passes through unchanged
(because x ⊕ 0 = x). The animation shows each operation step-by-step with color-
coding to track which pairs cancel and which number survives, making the algorithm's
mathematical beauty intuitive and clear."

**Rapid-Fire Version:**
- Input array has pairs and one single number
- XOR operation: x ⊕ x = 0 (pairs cancel), x ⊕ 0 = x (identity)
- Step-by-step: accumulate XOR of all elements
- Duplicates become 0 and cancel out
- Single number (x ⊕ 0 = x) survives at the end
- Color-coding tracks pair relationships and final result
- Time: O(n), Space: O(1) - optimal for the problem

**Ultra-Minimal One-Liner:**
"XOR all array elements: duplicate pairs cancel (x ⊕ x = 0), single number survives
(x ⊕ 0 = x), revealing the non-duplicate in linear time with constant space."
"""
