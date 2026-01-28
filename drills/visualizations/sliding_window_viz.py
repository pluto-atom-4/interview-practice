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


class SlidingWindowVisualization(Scene):
    """
    Visualization of the sliding window two-pointer algorithm for finding
    the longest substring without repeating characters.

    Uses "abcabcbb" as input to show:
    1. Initial window expansion
    2. Character collision detection
    3. Window shrinking when duplicate found
    4. All variable tracking with proper color coding:
       - last_seen dictionary: Updates with each new character
       - max_length (GREEN): Shows best substring length found
       - current_length (BLUE): Shows current window length each iteration
       - longest_substring (YELLOW): Shows best substring found
    """

    def construct(self):
        s = "abcabcbb"

        # Title
        title = Text("Sliding Window: Longest Unique Substring", font_size=32).to_edge(UP)
        self.play(Write(title))

        # Input string visualization
        string_label = Text("Input String:", font_size=20).to_edge(LEFT).shift(UP * 2.5)
        self.play(Write(string_label))

        # Create character boxes
        char_boxes = VGroup()
        char_texts = VGroup()
        for i, char in enumerate(s):
            box = Rectangle(width=0.6, height=0.6, color=BLUE, stroke_width=2)
            text = Text(char, font_size=20, color=WHITE).move_to(box.get_center())
            char_box = VGroup(box, text).move_to(ORIGIN + RIGHT * (i * 0.8) + UP * 1.5)
            char_boxes.add(box)
            char_texts.add(text)

        string_display = VGroup(char_boxes, char_texts)
        string_display.shift(RIGHT * 1.5)

        self.play(*[Create(box) for box in char_boxes])
        self.play(*[Write(text) for text in char_texts])

        # Variables section
        var_y_start = DOWN * 1

        # last_seen dictionary display
        dict_label = Text("last_seen: {}", font_size=16).move_to(var_y_start + LEFT * 4)
        self.play(Write(dict_label))

        # max_length display (GREEN)
        max_length_display = Text("max_length: 0", font_size=16, color=GREEN).move_to(var_y_start + RIGHT * 0.5)
        self.play(Write(max_length_display))

        # current_length display (BLUE)
        current_length_display = Text("current_length: 0", font_size=16, color=BLUE).move_to(var_y_start + DOWN * 1 + LEFT * 4)
        self.play(Write(current_length_display))

        # longest_substring display (YELLOW)
        longest_display = Text('longest: ""', font_size=16, color=YELLOW).move_to(var_y_start + DOWN * 1 + RIGHT * 0.5)
        self.play(Write(longest_display))

        # Algorithm state variables
        start_idx = 0
        last_seen = {}
        max_length = 0
        longest_substring = ""

        self.wait(1)

        # Process each character
        for i, char in enumerate(s):
            # Highlight current character being processed
            current_box = char_boxes[i]
            current_text = char_texts[i]
            self.play(Indicate(VGroup(current_box, current_text), color=RED, scale_factor=1.3))

            # Check if character collision
            collision = char in last_seen and last_seen[char] >= start_idx

            if collision:
                # Collision detected - highlight old occurrence
                old_idx = last_seen[char]
                old_box = char_boxes[old_idx]
                self.play(Indicate(old_box, color=RED, scale_factor=1.2))
                self.wait(0.3)

                # Move start pointer
                start_idx = last_seen[char] + 1

                # Clear highlights and update window
                for box in char_boxes:
                    box.set_color(BLUE)
                for j in range(start_idx, i + 1):
                    char_boxes[j].set_color(GREEN)
            else:
                # No collision - window expands naturally
                # Clear previous highlights
                for box in char_boxes:
                    box.set_color(BLUE)
                # Highlight current window
                for j in range(start_idx, i + 1):
                    char_boxes[j].set_color(GREEN)

            # Update last_seen dictionary
            last_seen[char] = i

            # Update dict display
            dict_text = self._format_dict(last_seen)
            new_dict_label = Text(f"last_seen: {dict_text}", font_size=16).move_to(var_y_start + LEFT * 4)
            self.play(FadeOut(dict_label), FadeIn(new_dict_label), run_time=0.2)
            dict_label = new_dict_label

            # Calculate current window length
            current_length = i - start_idx + 1
            current_window = s[start_idx:i + 1]

            # Update max_length if current is better
            if current_length > max_length:
                max_length = current_length
                longest_substring = current_window

            # Update max_length display (GREEN)
            new_max_display = Text(f"max_length: {max_length}", font_size=16, color=GREEN).move_to(var_y_start + RIGHT * 0.5)
            self.play(FadeOut(max_length_display), FadeIn(new_max_display), run_time=0.2)
            max_length_display = new_max_display

            # Update current_length display (BLUE)
            new_current_display = Text(f"current_length: {current_length}", font_size=16, color=BLUE).move_to(var_y_start + DOWN * 1 + LEFT * 4)
            self.play(FadeOut(current_length_display), FadeIn(new_current_display), run_time=0.2)
            current_length_display = new_current_display

            # Update longest_substring display (YELLOW)
            new_longest_display = Text(f'longest: "{longest_substring}"', font_size=16, color=YELLOW).move_to(var_y_start + DOWN * 1 + RIGHT * 0.5)
            self.play(FadeOut(longest_display), FadeIn(new_longest_display), run_time=0.2)
            longest_display = new_longest_display

            self.wait(0.7)

        # Final result with all variables visible
        self.wait(1)

        result_label = Text("Final Result:", font_size=20, color=WHITE).move_to(DOWN * 4)
        self.play(Write(result_label))

        result_box = Rectangle(width=3, height=0.8, color=YELLOW, stroke_width=2)
        result_text = Text(f'"{longest_substring}"', font_size=24, color=WHITE).move_to(result_box.get_center())
        result_display = VGroup(result_box, result_text).move_to(DOWN * 4.8)

        self.play(Create(result_box), Write(result_text))
        self.wait(2)

    def _format_dict(self, d: dict) -> str:
        """Format dictionary for display."""
        if not d:
            return "{}"
        items = [f"'{k}': {v}" for k, v in sorted(d.items())]
        return "{" + ", ".join(items) + "}"

