"""
## Rotated Binary Search Visualization

Shows step-by-step execution of modified binary search on a rotated sorted array.

The algorithm detects which half is sorted at each iteration by comparing nums[left] 
and nums[mid], then determines if the target falls within the sorted half's value range 
to decide which half to eliminate.

Example with concrete values:
Input: [4, 5, 6, 7, 0, 1, 2], target = 0
- Iteration 1: left=0, mid=3, right=6 → left half [4,5,6,7] is sorted; target not in range → search right
- Iteration 2: left=4, mid=5, right=6 → right half [1,2] is sorted; target not in range → search left
- Iteration 3: left=4, mid=4, right=4 → nums[4]=0 matches target → return 4

Visualizes:
1. Rotated sorted array as colored boxes (unsorted rotation point visible)
2. Left, mid, right pointers updating at each iteration
3. Sorted vs unsorted half detection with color highlighting
4. Target search space narrowing with visual elimination
5. Decision logic: which half to search based on target value
"""

from manim import (
    BLUE,
    DOWN,
    GRAY,
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
    Uncreate,
    VGroup,
    Write,
)


class RotatedBinarySearchVisualization(Scene):
    """
    Visualization of modified binary search on a rotated sorted array.
    
    The animation shows:
    1. Array display with elements as colored boxes
    2. Pointer positions (left, mid, right) updated each iteration
    3. Which half is detected as sorted (shaded background)
    4. Decision: target in sorted half? (yes → narrow; no → cross over)
    5. Search space narrowing until target found or exhausted
    """

    def construct(self):
        # === Scene Setup ===
        title = Text("Rotated Binary Search", font_size=28, color=WHITE)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # === Input and Target ===
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 0
        input_text = Text(f"Array: {nums}", font_size=14, color=BLUE)
        target_text = Text(f"Target: {target}", font_size=14, color=RED)
        input_text.move_to(ORIGIN + UP * 1.5 + LEFT * 2)
        target_text.move_to(ORIGIN + UP * 1.5 + RIGHT * 2)
        self.play(Write(input_text), Write(target_text))
        self.wait(0.5)

        # === Create Array Display ===
        # Position array elements left-to-right
        array_y = 0.5
        element_width = 0.6
        array_start_x = -2.5

        color_palette = [BLUE, YELLOW, GREEN, YELLOW, RED, GREEN, BLUE]
        array_elements = VGroup()
        element_boxes = []
        element_texts = []

        for i, (num, color) in enumerate(zip(nums, color_palette)):
            pos_x = array_start_x + i * element_width
            box = Rectangle(width=0.5, height=0.5, color=color, fill_opacity=0.3)
            box.move_to(ORIGIN + RIGHT * pos_x + DOWN * array_y)
            
            num_text = Text(str(num), font_size=12, color=WHITE)
            num_text.move_to(box.get_center())
            
            array_elements.add(box, num_text)
            element_boxes.append(box)
            element_texts.append(num_text)

        self.play(Create(array_elements))
        self.wait(0.5)

        # === Index Labels Below Array ===
        index_labels = VGroup()
        for i in range(len(nums)):
            pos_x = array_start_x + i * element_width
            idx_text = Text(str(i), font_size=10, color=GRAY)
            idx_text.move_to(ORIGIN + RIGHT * pos_x + DOWN * (array_y + 0.6))
            index_labels.add(idx_text)

        self.play(Create(index_labels))
        self.wait(0.3)

        # === Algorithm State Display (Left Panel) ===
        state_y_base = 0
        state_box_y = state_y_base
        state_labels = VGroup()
        
        left_label = Text("left:", font_size=12, color=BLUE)
        mid_label = Text("mid:", font_size=12, color=YELLOW)
        right_label = Text("right:", font_size=12, color=GREEN)
        
        left_label.move_to(LEFT * 3.5 + DOWN * state_box_y)
        mid_label.move_to(LEFT * 3.5 + DOWN * (state_box_y + 0.4))
        right_label.move_to(LEFT * 3.5 + DOWN * (state_box_y + 0.8))
        
        state_labels.add(left_label, mid_label, right_label)
        self.play(Create(state_labels))

        # === Algorithm Execution ===
        left, right = 0, len(nums) - 1
        iteration = 0
        state_values = None

        while left <= right:
            iteration += 1
            mid = (left + right) // 2

            # === Update State Display ===
            if state_values is not None:
                self.play(Uncreate(state_values))

            state_values = VGroup()
            left_val = Text(f"{left}", font_size=12, color=BLUE)
            mid_val = Text(f"{mid}", font_size=12, color=YELLOW)
            right_val = Text(f"{right}", font_size=12, color=GREEN)
            
            left_val.next_to(left_label, RIGHT, buff=0.3)
            mid_val.next_to(mid_label, RIGHT, buff=0.3)
            right_val.next_to(right_label, RIGHT, buff=0.3)
            
            state_values.add(left_val, mid_val, right_val)
            self.play(Write(state_values))

            # === Highlight Current Pointers ===
            left_box = element_boxes[left]
            mid_box = element_boxes[mid]
            right_box = element_boxes[right]

            self.play(
                Indicate(left_box, color=BLUE, scale_factor=1.3),
                Indicate(mid_box, color=YELLOW, scale_factor=1.3),
                Indicate(right_box, color=GREEN, scale_factor=1.3),
            )
            self.wait(0.3)

            # === Check if Target Found ===
            if nums[mid] == target:
                match_text = Text(f"Found! nums[{mid}] = {target}", font_size=14, color=RED)
                match_text.move_to(ORIGIN + DOWN * 2.0)
                self.play(Write(match_text))
                self.play(Indicate(mid_box, color=RED, scale_factor=1.5))
                self.wait(1)
                break

            # === Determine Sorted Half and Decision ===
            decision_text = None
            
            if nums[left] <= nums[mid]:
                # Left side is sorted
                decision = f"Left [{nums[left]}..{nums[mid]}] sorted"
                decision_text = Text(decision, font_size=11, color=BLUE)
                decision_text.move_to(ORIGIN + DOWN * 1.5)
                self.play(Write(decision_text))
                self.wait(0.3)

                if nums[left] <= target < nums[mid]:
                    # Target in left sorted half
                    action = f"{target} in [{nums[left]}..{nums[mid]}] → search LEFT"
                    action_text = Text(action, font_size=11, color=YELLOW)
                    action_text.move_to(ORIGIN + DOWN * 1.9)
                    self.play(Write(action_text))
                    right = mid - 1
                else:
                    # Target not in left half, search right
                    action = f"{target} not in [{nums[left]}..{nums[mid]}] → search RIGHT"
                    action_text = Text(action, font_size=11, color=YELLOW)
                    action_text.move_to(ORIGIN + DOWN * 1.9)
                    self.play(Write(action_text))
                    left = mid + 1
            else:
                # Right side is sorted
                decision = f"Right [{nums[mid]}..{nums[right]}] sorted"
                decision_text = Text(decision, font_size=11, color=GREEN)
                decision_text.move_to(ORIGIN + DOWN * 1.5)
                self.play(Write(decision_text))
                self.wait(0.3)

                if nums[mid] < target <= nums[right]:
                    # Target in right sorted half
                    action = f"{target} in [{nums[mid]}..{nums[right]}] → search RIGHT"
                    action_text = Text(action, font_size=11, color=YELLOW)
                    action_text.move_to(ORIGIN + DOWN * 1.9)
                    self.play(Write(action_text))
                    left = mid + 1
                else:
                    # Target not in right half, search left
                    action = f"{target} not in [{nums[mid]}..{nums[right]}] → search LEFT"
                    action_text = Text(action, font_size=11, color=YELLOW)
                    action_text.move_to(ORIGIN + DOWN * 1.9)
                    self.play(Write(action_text))
                    right = mid - 1

            self.wait(0.5)

            # === Fade Out Decision Text ===
            if decision_text is not None:
                self.play(FadeOut(decision_text), FadeOut(action_text))

            self.wait(0.3)

        # === Final Summary ===
        if state_values is not None:
            self.play(Uncreate(state_values))

        summary = Text(f"Search completed in {iteration} iterations", font_size=14, color=GREEN)
        summary.move_to(ORIGIN + DOWN * 2.2)
        self.play(Write(summary))

        complexity = Text("Time: O(log n)  Space: O(1)", font_size=12, color=GRAY)
        complexity.move_to(ORIGIN + DOWN * 2.6)
        self.play(Write(complexity))

        self.wait(1)
