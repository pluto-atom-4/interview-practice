"""
Merge Sort Visualization with Enhanced Phase Visibility.

Visualizes merge sort with clear, animated divide and merge phases.
Bars move and change visibly during both phases.
"""

from __future__ import annotations

from manim import (
    BLUE,
    GREEN,
    RED,
    YELLOW,
    DOWN,
    UP,
    LEFT,
    RIGHT,
    Indicate,
    Rectangle,
    Scene,
    Text,
    VGroup,
    rate_functions,
    AnimationGroup,
)


class MergeSortVisualization(Scene):
    """
    Enhanced merge sort with visible phase animations.
    
    - Divide phase: bars separate and color-code visibly
    - Merge phase: bars visibly rearrange to sorted order
    - Resolution: 800x600
    """

    def construct(self):
        """Create the merge sort visualization."""
        values = [38, 27, 43, 3, 9, 82, 10]
        max_val = max(values)
        
        # Create bars with proper alignment
        bars = self.create_bar_chart(values, max_val)
        self.add(bars)
        self.wait(1)
        
        # Divide phase - bars separate and change colors
        self.divide_phase(bars, values)
        self.wait(1.5)
        
        # Merge phase - bars animate to sorted positions and heights
        self.merge_phase(bars, values, max_val)
        self.wait(2)

    def create_bar_chart(self, values: list, max_val: int) -> VGroup:
        """Create bars aligned at y=0 with larger scale."""
        bars = VGroup()
        
        bar_width = 0.6
        spacing = 0.3
        scale = 3.2 / max_val  # Increased from 2.8 to 3.2
        total_width = len(values) * (bar_width + spacing)
        start_x = -total_width / 2
        baseline_y = -0.8  # Move baseline down from 0 to -0.8
        
        for i, val in enumerate(values):
            height = val * scale
            x = start_x + i * (bar_width + spacing) + bar_width / 2
            
            bar = Rectangle(
                width=bar_width,
                height=height,
                fill_color=BLUE,
                fill_opacity=0.7,
                stroke_width=2,
            )
            bar.shift([x, baseline_y + height / 2, 0])
            bars.add(bar)
        
        return bars

    def divide_phase(self, bars: VGroup, values: list):
        """
        Divide phase with visible separation and color changes.
        
        Bars separate into groups and change colors to show division.
        """
        mid = len(values) // 2
        
        # Animate left half moving left and turning red
        left_anims = []
        for i in range(mid):
            left_anims.append(bars[i].animate.shift(LEFT * 0.5).set_color(RED))
        
        if left_anims:
            self.play(AnimationGroup(*left_anims, lag_ratio=0.1), run_time=1.0)
        
        self.wait(0.5)
        
        # Animate right half moving right and turning yellow
        right_anims = []
        for i in range(mid, len(values)):
            right_anims.append(bars[i].animate.shift(RIGHT * 0.5).set_color(YELLOW))
        
        if right_anims:
            self.play(AnimationGroup(*right_anims, lag_ratio=0.1), run_time=1.0)
        
        self.wait(0.5)
        
        # Move bars back to original positions
        back_anims = []
        for i in range(len(bars)):
            if i < mid:
                back_anims.append(bars[i].animate.shift(RIGHT * 0.5))
            else:
                back_anims.append(bars[i].animate.shift(LEFT * 0.5))
        
        if back_anims:
            self.play(AnimationGroup(*back_anims, lag_ratio=0.1), run_time=1.0)
        
        self.wait(0.5)

    def merge_phase(self, bars: VGroup, values: list, max_val: int):
        """
        Merge phase with visible bar rearrangement and height changes.
        
        Bars animate to sorted positions and heights.
        """
        sorted_vals = sorted(values)
        scale = 3.2 / max_val
        bar_width = 0.6
        spacing = 0.3
        total_width = len(values) * (bar_width + spacing)
        start_x = -total_width / 2
        baseline_y = -0.8
        
        # Show comparison animations with movement
        comparisons = [
            (1, 0, "27 < 38"),
            (2, 3, "43 > 3"),
            (0, 2, "27 < 43"),
            (1, 3, "38 < 43"),
        ]
        
        for i, j, _ in comparisons:
            if i < len(bars) and j < len(bars):
                self.play(
                    Indicate(bars[i], color=YELLOW, scale_factor=1.2),
                    Indicate(bars[j], color=YELLOW, scale_factor=1.2),
                    run_time=0.4,
                )
                self.wait(0.2)
        
        self.wait(0.5)
        
        # Create sorted bars with new positions and heights
        # Group bars into sorted positions with animations
        animations = []
        
        for i, sorted_val in enumerate(sorted_vals):
            old_bar = bars[i]
            new_height = sorted_val * scale
            x = start_x + i * (bar_width + spacing) + bar_width / 2
            
            # Create new bar
            new_bar = Rectangle(
                width=bar_width,
                height=new_height,
                fill_color=GREEN,
                fill_opacity=0.7,
                stroke_width=2,
            )
            new_bar.shift([x, baseline_y + new_height / 2, 0])
            
            # Animate transformation
            animations.append(old_bar.animate.become(new_bar))
        
        # Play all animations with staggered timing for visibility
        if animations:
            self.play(AnimationGroup(*animations, lag_ratio=0.08), run_time=2.0)
        
        self.wait(0.5)
        
        # Highlight final sorted bars
        for bar in bars:
            self.play(
                Indicate(bar, color=GREEN, scale_factor=1.1),
                run_time=0.2,
            )
        
        self.wait(1)
