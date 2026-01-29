"""
## Operation Overview

Reverses a singly linked list by iteratively rearranging node pointers using the three-pointer technique.

Shows the step-by-step transformation using the three-pointer algorithm:
- prev: tracks the reversed portion (initially None)
- current: the node being processed
- nxt: saves the reference before pointer reversal

Example with concrete values:
Original:  1 → 2 → 3 → None
Reversed:  3 → 2 → 1 → None

Visualizes:
1. Original linked list with forward pointers
2. Three pointers (prev, current, nxt) at each step
3. Pointer reversal happening in real-time with arrows
4. Progressive transformation showing the reversed segment growing
5. Final state with all pointers reversed and new head established
"""

from manim import (
    BLACK,
    BLUE,
    DOWN,
    GREEN,
    LEFT,
    ORANGE,
    ORIGIN,
    PINK,
    PURPLE,
    RED,
    RIGHT,
    TEAL,
    UP,
    WHITE,
    YELLOW,
    Arrow,
    Circle,
    Create,
    FadeIn,
    FadeOut,
    Indicate,
    Line,
    Rectangle,
    Scene,
    Text,
    Uncreate,
    VGroup,
    Write,
    config,
)


class ReverseLinkedListVisualization(Scene):
    """
    Visualization of iterative linked list reversal using three pointers.

    Shows how the three-pointer technique transforms forward pointers into backward
    pointers through a single pass. Each iteration captures the next reference before
    reversing the current pointer, then advances all pointers. The animation makes
    the state transitions and pointer relationships explicit through color-coding
    and arrow animations.
    """

    def construct(self):
        # Canvas Bounds: x in [-3.8, 3.8], y in [-2.2, 2.2]
        # Layout Strategy:
        # - Title: y = 2.0 (top)
        # - Algorithm text: y = 1.2 (below title)
        # - Linked list nodes: y = -0.3 (center)
        # - Pointer labels: x = -3.5, y = 0.5 to 2.0 (left panel)
        # - Step counter: y = -2.1 (bottom)

        # Color Scheme
        # - BLUE: prev pointer and reversed segment
        # - RED: current pointer and node being processed
        # - GREEN: nxt pointer and unreversed segment
        # - YELLOW: nodes in the reversed segment
        # - WHITE: nodes yet to be processed
        # - PURPLE: pointer arrows for next references
        # - ORANGE: new pointer after reversal

        # Title at y=2.0 (safe: < 2.2)
        title = Text("Linked List Reversal (Three-Pointer)", font_size=22, color=WHITE)
        title.move_to(ORIGIN + UP * 2.0)
        self.play(Write(title))
        self.wait(0.8)

        # Algorithm explanation at y=1.2
        algo_text = Text(
            "prev→curr→nxt | Reverse: curr.next=prev",
            font_size=12,
            color=WHITE,
        )
        algo_text.move_to(ORIGIN + UP * 1.2)
        self.play(Write(algo_text))
        self.wait(0.8)

        # Create linked list data
        values = [1, 2, 3]
        self._create_and_reverse_list(values)

    def _create_and_reverse_list(self, values):
        """Create a linked list visualization and animate its reversal."""
        # Canvas: x in [-3.8, 3.8], y in [-2.2, 2.2]
        # Nodes will be positioned at y = -0.3 (center)
        # Three nodes with 2.0 spacing: -2.0, 0.0, +2.0 (all within ±3.8)

        nodes = VGroup()
        pointers = []

        node_y = -0.3
        node_start_x = -2.0  # Leftmost node at x=-2.0
        node_spacing = 2.0   # Gap between nodes

        for i, val in enumerate(values):
            x = node_start_x + i * node_spacing
            # Verify x is within bounds [-3.8, 3.8]
            if not (-3.8 <= x <= 3.8):
                print(f"WARNING: Node {val} at x={x} may be outside canvas bounds")

            node_circle = Circle(radius=0.35, color=WHITE, fill_color=WHITE, fill_opacity=0.1)
            node_circle.move_to(ORIGIN + RIGHT * x + DOWN * node_y)

            node_text = Text(str(val), font_size=16, color=WHITE)
            node_text.move_to(node_circle.get_center())

            nodes.add(node_circle)
            nodes.add(node_text)
            pointers.append(node_circle.get_center())

        # Create initial forward pointers
        forward_arrows = VGroup()
        for i in range(len(pointers) - 1):
            arrow = Arrow(
                pointers[i] + RIGHT * 0.45,
                pointers[i + 1] + LEFT * 0.45,
                buff=0,
                color=PURPLE,
                stroke_width=1.5,
            )
            forward_arrows.add(arrow)

        # Add None label at far right (x < 3.8)
        none_label = Text("None", font_size=11, color=PURPLE)
        none_label.move_to(ORIGIN + RIGHT * 3.5 + DOWN * node_y)

        # Display initial list
        self.play(Create(nodes))
        self.play(Create(forward_arrows), Write(none_label))
        self.wait(0.8)

        # Animate three-pointer reversal
        self._animate_reversal(nodes, pointers, values, node_y)

    def _animate_reversal(self, nodes, pointers, values, node_y):
        """Animate the three-pointer reversal process step by step."""
        # Canvas bounds: x in [-3.8, 3.8], y in [-2.2, 2.2]
        # Text management: Uncreate old before creating new to avoid accumulation

        n = len(values)
        node_start_x = -2.0
        node_spacing = 2.0

        # Left panel labels (x = -3.5, persistent)
        left_panel_x = -3.5
        
        prev_label = Text("prev:", font_size=11, color=BLUE)
        prev_label.move_to(ORIGIN + RIGHT * left_panel_x + DOWN * (node_y - 0.8))

        curr_label = Text("curr:", font_size=11, color=RED)
        curr_label.move_to(ORIGIN + RIGHT * left_panel_x + DOWN * (node_y - 1.4))

        nxt_label = Text("nxt:", font_size=11, color=GREEN)
        nxt_label.move_to(ORIGIN + RIGHT * left_panel_x + DOWN * (node_y - 2.0))

        self.play(Write(prev_label), Write(curr_label), Write(nxt_label))
        self.wait(0.3)

        # Initial pointers and text state tracking
        prev_ptr = None
        current_ptr = 0
        reversed_portion = []
        
        # Track current state text elements for cleanup
        state_text_group = None
        step_counter = None

        for step in range(n):
            # Get pointers
            nxt_ptr = current_ptr + 1 if current_ptr + 1 < n else None

            # UPDATE STEP COUNTER (remove old, add new)
            if step_counter is not None:
                self.play(Uncreate(step_counter))
            
            step_counter = Text(
                f"Step {step + 1}: Reverse node {values[current_ptr]}",
                font_size=10,
                color=WHITE,
            )
            step_counter.move_to(ORIGIN + DOWN * 2.15)
            self.play(Write(step_counter))

            # Highlight current node
            current_node_group = self._get_node_group(nodes, current_ptr)
            self.play(Indicate(current_node_group, color=RED, scale_factor=1.2))

            # SHOW STATE VALUES (remove old, add new)
            if state_text_group is not None:
                self.play(Uncreate(state_text_group))
            
            state_text_group = VGroup()
            
            prev_state = "None" if prev_ptr is None else f"N{values[prev_ptr]}"
            curr_state = f"N{values[current_ptr]}"
            nxt_state = "None" if nxt_ptr is None else f"N{values[nxt_ptr]}"

            prev_val_text = Text(prev_state, font_size=9, color=BLUE)
            prev_val_text.move_to(ORIGIN + RIGHT * (left_panel_x + 0.7) + DOWN * (node_y - 0.8))

            curr_val_text = Text(curr_state, font_size=9, color=RED)
            curr_val_text.move_to(ORIGIN + RIGHT * (left_panel_x + 0.7) + DOWN * (node_y - 1.4))

            nxt_val_text = Text(nxt_state, font_size=9, color=GREEN)
            nxt_val_text.move_to(ORIGIN + RIGHT * (left_panel_x + 0.7) + DOWN * (node_y - 2.0))

            state_text_group.add(prev_val_text, curr_val_text, nxt_val_text)
            self.play(Write(state_text_group))
            self.wait(0.4)

            # Step 1: Show saving nxt reference
            nxt_save_arrow = None
            if nxt_ptr is not None:
                nxt_x = node_start_x + nxt_ptr * node_spacing
                nxt_node_pos = ORIGIN + RIGHT * nxt_x + DOWN * node_y
                nxt_save_arrow = Arrow(
                    pointers[current_ptr] + RIGHT * 0.4,
                    nxt_node_pos + LEFT * 0.4,
                    buff=0,
                    color=GREEN,
                    stroke_width=1.5,
                )
                self.play(Create(nxt_save_arrow))
                self.wait(0.3)

            # Step 2: Reverse the pointer
            if prev_ptr is not None:
                prev_x = node_start_x + prev_ptr * node_spacing
                prev_node_pos = ORIGIN + RIGHT * prev_x + DOWN * node_y
            else:
                prev_node_pos = ORIGIN + RIGHT * (-3.4) + DOWN * node_y

            current_node_pos = pointers[current_ptr]
            reverse_arrow = Arrow(
                current_node_pos + RIGHT * 0.4,
                prev_node_pos + LEFT * 0.4,
                buff=0,
                color=ORANGE,
                stroke_width=1.5,
            )
            self.play(Create(reverse_arrow))
            self.wait(0.3)

            # Step 3: Move prev and current forward
            prev_ptr = current_ptr
            current_ptr = nxt_ptr
            reversed_portion.append(prev_ptr)

            # Highlight nodes in reversed segment
            for idx in reversed_portion:
                node_circle = self._get_node_circle(nodes, idx)
                self.play(node_circle.animate.set_fill(YELLOW, opacity=0.3), run_time=0.15)

            # CLEANUP: Remove state text and arrows
            self.play(
                Uncreate(state_text_group),
                Uncreate(reverse_arrow),
            )

            if nxt_save_arrow is not None:
                self.play(Uncreate(nxt_save_arrow))

            self.wait(0.2)

        # FINAL CLEANUP: Replace step counter with completion message
        if step_counter is not None:
            self.play(Uncreate(step_counter))
        
        final_text = Text("✓ All nodes reversed!", font_size=11, color=WHITE)
        final_text.move_to(ORIGIN + DOWN * 2.15)
        self.play(Write(final_text))
        self.wait(1.2)

    def _get_node_group(self, nodes, index):
        """Get the VGroup containing both circle and text for a node."""
        return VGroup(nodes[index * 2], nodes[index * 2 + 1])

    def _get_node_circle(self, nodes, index):
        """Get just the circle for a node."""
        return nodes[index * 2]
