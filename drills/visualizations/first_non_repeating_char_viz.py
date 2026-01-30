"""
## Operation Overview

Find the first non-repeating character in a string using a two-pass hash table approach.

Shows the step-by-step transformation using:
Pass 1: Count character frequencies → Hash table {char: count}
Pass 2: Scan string, return first character where count == 1

Example with concrete values:
Input: "abacabad"
Pass 1 (counting): a→3, b→2, c→1, d→1
Pass 2 (searching): Check 'a' (count=3, skip), 'b' (count=2, skip), 'a' (count=3, skip), 
                    'c' (count=1, FOUND!)
Output: 'c'

Visualizes:
1. Original string with character positions
2. Hash table building during first pass (frequency counting)
3. Character-by-character scanning during second pass
4. Visual highlight when target character is found
5. Final result with explanation
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
    Transform,
    VGroup,
    Write,
)


class FirstNonRepeatingCharViz(Scene):
    """
    Visualization of the first non-repeating character algorithm.

    This scene demonstrates:
    - Pass 1: Iterating through string and building frequency hash table
    - Pass 2: Scanning string to find first character with frequency = 1
    - Visual distinction between counting phase and search phase
    - Color-coded highlighting for the found character
    """

    def construct(self):
        # ===== SCENE LAYOUT STRATEGY =====
        # - Title at top
        # - Original string on left side (tracking current position)
        # - Hash table (frequency counter) in center
        # - Status/result on right side
        # Canvas layout:
        #   Title (UP at y=2.0)
        #   ┌─────────────┬──────────────┬──────────────┐
        #   │   String    │ Freq Table   │   Status     │
        #   │   (LEFT)    │   (CENTER)   │   (RIGHT)    │
        #   └─────────────┴──────────────┴──────────────┘
        #   Instructions/Result (DOWN at y=-2.0)

        # ===== COLOR SCHEME =====
        # - BLUE: String characters (initial state)
        # - RED: Current character being processed
        # - GREEN: Hash table values
        # - YELLOW: Frequency count updates
        # - PURPLE: Pass indicator
        # - ORANGE: Found character (target)

        # ===== ANIMATION FLOW =====
        # 1. Title and setup (0.5s write + 0.5s wait)
        # 2. Display input string (0.5s create)
        # 3. Pass 1 label and intro (0.5s write + 0.5s wait)
        # 4. Build hash table character-by-character (0.3s per character)
        # 5. Pass 2 label and intro (0.5s write + 0.5s wait)
        # 6. Scan string to find first with count=1 (0.4s per character)
        # 7. Result display (1s write + 1s wait)

        input_string = "abacabad"
        expected_result = "c"

        # ===== TITLE =====
        title = Text("First Non-Repeating Character", font_size=24)
        title.move_to(ORIGIN + UP * 2.2)
        self.play(Write(title))
        self.wait(0.5)

        # ===== STEP 1: DISPLAY INPUT STRING =====
        step_title = Text("Input String:", font_size=16, color=BLUE)
        step_title.move_to(ORIGIN + LEFT * 3.0 + UP * 1.2)
        self.play(Write(step_title))

        # Create visual representation of string (each character in a box)
        string_chars = VGroup()
        char_boxes = {}
        char_width = 0.5
        start_x = -2.0  # Starting position (left side)

        for i, ch in enumerate(input_string):
            box = Rectangle(width=0.4, height=0.4, color=BLUE)
            char_text = Text(ch, font_size=12)

            # Position character boxes left to right with consistent spacing
            pos_x = start_x + i * char_width
            box.move_to(ORIGIN + RIGHT * pos_x + UP * 0.5)
            char_text.move_to(box.get_center())

            string_chars.add(box, char_text)
            char_boxes[i] = (box, char_text)

        self.play(Create(string_chars))
        self.wait(0.5)

        # ===== STEP 2: PASS 1 - COUNTING FREQUENCIES =====
        pass1_label = Text("PASS 1: Count Frequencies", font_size=14, color=PURPLE)
        pass1_label.move_to(ORIGIN + UP * 0.8)
        self.play(Write(pass1_label))
        self.wait(0.5)

        # Create hash table display area
        freq_title = Text("Frequency Table:", font_size=14, color=GREEN)
        freq_title.move_to(ORIGIN + DOWN * 0.5)
        self.play(Write(freq_title))

        # Create frequency table entries dynamically
        freq_display = {}
        freq_counter = {}

        for char_idx, ch in enumerate(input_string):
            # Update character highlight (show which character is being processed)
            highlight = Indicate(char_boxes[char_idx][0], color=RED, scale_factor=1.3)
            self.play(highlight, run_time=0.2)

            # Update frequency counter
            if ch not in freq_counter:
                freq_counter[ch] = 0
            freq_counter[ch] += 1

            # Remove old frequency entry if it exists
            if ch in freq_display:
                self.play(FadeOut(freq_display[ch]))

            # Create new frequency entry
            freq_text = Text(f"{ch}: {freq_counter[ch]}", font_size=12, color=GREEN)
            # Position below freq_title (at DOWN * 0.5) with vertical spacing
            # Start at DOWN * 1.0 (0.5 units below title) and stack downward
            entry_y = 1.0 + (list(freq_counter.keys()).index(ch)) * 0.3
            freq_text.move_to(ORIGIN + DOWN * entry_y)
            freq_display[ch] = freq_text

            self.play(Write(freq_text), run_time=0.2)
            self.wait(0.2)

        self.wait(0.5)

        # ===== STEP 3: PASS 2 - SEARCH FOR FIRST NON-REPEATING =====
        self.play(FadeOut(pass1_label))

        pass2_label = Text("PASS 2: Find First with Count=1", font_size=14, color=PURPLE)
        pass2_label.move_to(ORIGIN + UP * 0.8)
        self.play(Write(pass2_label))
        self.wait(0.5)

        # Scan through string looking for count=1
        found_char = None
        found_idx = None

        for char_idx, ch in enumerate(input_string):
            # Highlight current character being checked
            highlight = Indicate(char_boxes[char_idx][0], color=YELLOW, scale_factor=1.3)
            self.play(highlight, run_time=0.2)

            # Create status text showing current check
            status = Text(f"Checking '{ch}': count={freq_counter[ch]}", font_size=11, color=GRAY)
            status.move_to(ORIGIN + RIGHT * 3.0 + DOWN * 0.2)
            self.play(Write(status), run_time=0.1)

            if freq_counter[ch] == 1 and found_char is None:
                # Found it!
                found_char = ch
                found_idx = char_idx
                self.play(FadeOut(status))
                break

            self.wait(0.2)
            self.play(FadeOut(status), run_time=0.1)

        self.wait(0.5)

        # ===== STEP 4: HIGHLIGHT RESULT =====
        if found_char:
            # Highlight the found character
            result_box, result_text = char_boxes[found_idx]
            self.play(Indicate(result_box, color=ORANGE, scale_factor=1.5), run_time=0.5)

            # Display result
            result_label = Text(f"Result: '{found_char}'", font_size=16, color=ORANGE)
            result_label.move_to(ORIGIN + DOWN * 2.0)
            self.play(Write(result_label), run_time=0.5)
        else:
            # No non-repeating character found
            result_label = Text("Result: None (All characters repeat)", font_size=14, color=RED)
            result_label.move_to(ORIGIN + DOWN * 2.0)
            self.play(Write(result_label), run_time=0.5)

        self.wait(1.0)

        # ===== COMPLEXITY INFO =====
        complexity = Text(
            "Time: O(n)  Space: O(k)", font_size=11, color=GRAY
        )
        complexity.move_to(ORIGIN + DOWN * 2.5)
        self.play(Write(complexity), run_time=0.3)
        self.wait(1.0)
