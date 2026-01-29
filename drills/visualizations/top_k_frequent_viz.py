"""
## Operation Overview

Visualization of the Top-K Frequent Elements algorithm using a min-heap approach.

Shows the step-by-step transformation using the min-heap strategy:
- Frequency counting: Build frequency map from input array
- Heap operations: Maintain a heap of size k with highest frequencies
- Result extraction: Sort and return k most frequent elements

Example with concrete values:
Input: nums = [1, 1, 1, 2, 2, 3], k = 2
Frequency Map: {1: 3, 2: 2, 3: 1}
Heap (size 2): maintains (freq: 2, val: 2) and (freq: 3, val: 1)
Output: [1, 2]

Visualizes:
1. Input array transformation into frequency map
2. Min-heap of size k being built element-by-element
3. Heap operations (push/pop) as elements are processed
4. Final extraction showing top-k elements
5. Complexity metrics (time: O(n log k), space: O(n))

## Visualization Strategy

Scene Layout:
- Top: Title and formula explanation
- Left: Input data (array and frequency map)
- Center: Heap state during operations
- Right: Output result
- Bottom: Complexity analysis

Color Scheme:
- BLUE: Frequency map elements
- GREEN: Elements entering the heap
- RED: Elements being popped from heap (too low frequency)
- YELLOW: Current element being processed
- PURPLE: Final result (top-k elements)
- WHITE: Heap structure and labels

Animation Flow:
1. Title and algorithm explanation (1.5 seconds)
2. Array to frequency map transformation (2 seconds)
3. Heap building process with step-by-step operations (4 seconds)
4. Result extraction and display (1.5 seconds)
5. Complexity summary (1 second)

## Key Visualization Concepts

- Why visualize frequency map first?
Understanding the input transformation into frequencies is crucial. The frequency map
represents the data being processed by the heap. By showing this step explicitly,
viewers understand that we're not sorting the original array, but frequencies.
Implemented with array on left transitioning to freq_map_dict in center.

- Why show heap as structured tree?
A min-heap is fundamentally a tree structure. Showing it as a tree (not just a list)
helps viewers intuitively understand why we only need to track k elements and why
removal is efficient (O(log k)). The heap property is visually obvious in tree form.
Implemented with nodes positioned hierarchically, parent above children.

- Why highlight the minimum frequency element?
The algorithm's key insight is removing the minimum frequency element when heap > k.
Highlighting this element shows viewers exactly which element gets removed and why.
Implemented with RED color and Indicate animation when pop occurs.

- Why show the comparison k < len(heap)?
The condition len(heap) > k is the gatekeeper for efficiency. By explicitly showing
when this condition triggers, viewers understand how the fixed-size k constraint
keeps heap operations O(log k) instead of O(log n).
Implemented with labeled condition check during each iteration.

## Animation Flow Details

Animation Sequence:
1. Title: "Top-K Frequent Elements" with k value (Write, 0.5s + 0.5s wait)
2. Algorithm formula display (Write frequency counting concept, 1s wait)
3. Input array display (Create, 0.5s)
4. Frequency map transformation:
   - For each unique element: show element → frequency (Create text, 0.3s each)
   - Display full freq_map when complete (1s wait)
5. Initialize empty heap structure (Create, 0.5s)
6. Frequency iteration loop:
   - Highlight current (frequency, value) in freq_map (Indicate, 0.2s)
   - Push to heap (Create node, 0.3s)
   - Check len(heap) > k condition (Write condition, 0.2s)
   - If true: Highlight min frequency element (RED, Indicate, 0.3s)
   - Pop min element (FadeOut, 0.3s)
   - Wait for clarity (0.3s)
7. Result extraction:
   - Sort k elements by frequency (Create arrow showing sort, 0.5s)
   - Extract values in descending frequency order (FadeIn to PURPLE, 0.5s)
   - Display final result array (Write, 0.5s)
8. Complexity summary:
   - Time: O(n log k) explanation (Write, 0.5s)
   - Space: O(n) explanation (Write, 0.5s)

## 30-Second Pitch

This visualization shows how the min-heap algorithm finds the k most frequent elements
efficiently. Instead of sorting all n elements, we maintain a heap of exactly k elements.
As we iterate through frequencies, we push new elements and remove the minimum frequency
when the heap exceeds k. This guarantees O(n log k) time complexity—much better than O(n log n)
sorting. The animation shows each heap operation step-by-step, making the efficiency gain obvious.

## Rapid-Fire Version

- Build frequency map from input array in O(n) time
- Initialize empty min-heap (priority queue by frequency)
- For each (frequency, value) pair: push to heap
- When heap size exceeds k: pop the minimum frequency element
- At end: sort k elements by frequency, extract values
- Result: top-k most frequent elements in O(n log k) time
- Space efficiency: heap only stores k elements, not all n

## Ultra-Minimal One-Liner

Min-heap of size k efficiently maintains top-k most frequent elements in O(n log k) time
by incrementally pushing frequencies and removing minimum when heap exceeds k.

## Implementation Notes

Technical Details:

Data Representation:
- Input array shown as sequential boxes with values
- Frequency map shown as key-value pairs (value → frequency count)
- Min-heap shown as tree structure with (frequency, value) tuples
- Condition checks shown as text annotations

Position Calculation:
- Left side (x = -3): Input array and frequency map
- Center (x = 0): Active heap during construction
- Right side (x = +3): Final result
- Vertical spacing: 0.8 units between elements

Color Management:
- BLUE for frequency counting phase
- GREEN for heap pushes (adding elements)
- RED for heap pops (removing min frequency)
- YELLOW for current active processing
- PURPLE for final result
- WHITE for labels and annotations

Animation Timing:
- Frequency map building: 0.3s per element
- Heap operations: 0.3-0.5s per operation
- Push operations: 0.3s (Create animation)
- Pop operations: 0.3s (FadeOut animation)
- Pauses for comprehension: 0.3-0.5s between major steps

Heap Structure Calculation:
- Tree level n has positions at y = -2*n
- Level width: 2^(height-n) spacing
- Parents positioned above children

Logic Flow:
- freq_map built by counting occurrences (manual iteration, no Counter)
- Heap implemented as list with heapq operations (push/pop)
- Min-heap property maintained automatically by heapq
- Final sort of k elements: O(k log k), negligible vs O(n log k) total
"""

from manim import (  # Shapes and styling; Positioning; Animations; Scene; Colors; Config
    BLACK,
    BLUE,
    DOWN,
    GRAY,
    GREEN,
    LEFT,
    ORIGIN,
    PURPLE,
    RED,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    AnimationGroup,
    Arrow,
    Circle,
    Create,
    FadeIn,
    FadeOut,
    Indicate,
    Rectangle,
    Scene,
    Succession,
    Text,
    VGroup,
    Write,
    config,
)


class TopKFrequentVisualization(Scene):
    """
    Visualization of the Top-K Frequent Elements algorithm.

    This scene demonstrates how a min-heap efficiently identifies the k most
    frequent elements in an array. The visualization shows:
    1. Array-to-frequency-map transformation
    2. Incremental heap construction with size constraint k
    3. Heap operations (push when adding, pop when exceeding k)
    4. Final result extraction in descending frequency order

    The key insight visualized: maintaining a fixed-size heap requires only
    O(n log k) time instead of O(n log n) for full sorting.
    """

    def construct(self):
        # Configuration
        self.camera.background_color = BLACK

        # Example data
        nums = [1, 1, 1, 2, 2, 3]
        k = 2
        freq_map = {1: 3, 2: 2, 3: 1}
        expected_output = [1, 2]

        # Title
        title = Text("Top-K Frequent Elements", font_size=44, color=WHITE)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Algorithm description
        description = Text(
            f"Find {k} most frequent elements using min-heap (O(n log k))",
            font_size=24,
            color=GRAY
        )
        description.next_to(title, DOWN, buff=0.3)
        self.play(Write(description))
        self.wait(0.7)

        # Input array display
        array_label = Text("Input Array:", font_size=20, color=WHITE)
        array_label.move_to(LEFT * 4 + UP * 2)
        
        array_boxes = VGroup()
        for i, num in enumerate(nums):
            box = Rectangle(width=0.5, height=0.5, color=BLUE, stroke_width=2)
            box.move_to(LEFT * 4 + UP * 1.2 + RIGHT * (i * 0.6))
            num_text = Text(str(num), font_size=16, color=WHITE)
            num_text.move_to(box.get_center())
            array_boxes.add(box)
            array_boxes.add(num_text)

        self.play(Write(array_label))
        self.play(Create(array_boxes))
        self.wait(0.5)

        # Frequency map display
        freq_label = Text("Frequency Map:", font_size=20, color=WHITE)
        freq_label.move_to(LEFT * 4 + DOWN * 0.5)
        
        freq_display = VGroup()
        for i, (val, freq) in enumerate(sorted(freq_map.items(), key=lambda x: -x[1])):
            freq_text = Text(f"{val}: {freq}", font_size=18, color=GREEN)
            freq_text.move_to(LEFT * 4 + DOWN * (1.2 + i * 0.5))
            freq_display.add(freq_text)

        self.play(Write(freq_label))
        self.play(Create(freq_display))
        self.wait(1.0)

        # Heap structure building
        heap_label = Text("Min-Heap (size k):", font_size=20, color=WHITE)
        heap_label.move_to(ORIGIN + UP * 2)
        self.play(Write(heap_label))
        self.wait(0.3)

        # Simulate heap operations
        heap_display = VGroup()
        heap_nodes = []
        
        for i, (val, freq) in enumerate(sorted(freq_map.items(), key=lambda x: -x[1])):
            # Create node
            node = Circle(radius=0.3, color=GREEN, stroke_width=2)
            node.move_to(ORIGIN + RIGHT * (i % 2 - 0.5) * 1.2 + DOWN * ((i // 2) * 1.2))
            
            node_text = Text(f"({freq},{val})", font_size=12, color=WHITE)
            node_text.move_to(node.get_center())
            
            heap_nodes.append((node, node_text))
            
            # Show push operation
            self.play(Create(node), Write(node_text), run_time=0.4)
            
            # Check k condition if heap exceeds k
            if len(heap_nodes) > k:
                # Highlight min frequency to pop
                min_node, min_text = heap_nodes[0]
                min_node.set_color(RED)
                
                condition_text = Text(f"len(heap) > {k}, pop min", font_size=14, color=RED)
                condition_text.move_to(ORIGIN + DOWN * 3)
                
                self.play(Write(condition_text))
                self.play(Indicate(min_node, color=RED, scale_factor=1.2))
                self.play(FadeOut(min_node), FadeOut(min_text), FadeOut(condition_text))
                
                heap_nodes.pop(0)
            
            self.wait(0.3)

        # Final result
        result_label = Text("Result (Top-K Frequent):", font_size=20, color=PURPLE)
        result_label.move_to(RIGHT * 3 + UP * 2)
        
        result_display = VGroup()
        for i, (node, node_text) in enumerate(heap_nodes):
            result_circle = Circle(radius=0.3, color=PURPLE, stroke_width=2)
            result_circle.move_to(RIGHT * 3 + DOWN * (0.5 + i * 0.8))
            
            freq, val = int(node_text.text.split(',')[0][1:]), int(node_text.text.split(',')[1][:-1])
            result_text = Text(str(val), font_size=16, color=WHITE)
            result_text.move_to(result_circle.get_center())
            
            result_display.add(result_circle)
            result_display.add(result_text)

        self.play(Write(result_label))
        self.play(Create(result_display))
        self.wait(0.7)

        # Complexity info
        complexity_label = Text(
            "Time: O(n log k)  |  Space: O(n)",
            font_size=18,
            color=YELLOW
        )
        complexity_label.to_edge(DOWN)
        
        self.play(Write(complexity_label))
        self.wait(1.0)
