---
name: visualize-using-manim
description: "Create comprehensive algorithm visualizations using Manim animations. Documents step-by-step transformations with formulas, color-coding, arrows, and multiple explanation formats. Use when building visual explanations for data structure operations, algorithmic transformations, or educational demonstrations."
license: Proprietary. LICENSE.txt has complete terms
---

# Visualize Using Manim Skill

## Overview

This skill provides a structured approach to creating algorithm visualizations using Manim (Mathematical Animation Engine). It guides you through designing clear, step-by-step animations that explain complex operations through visual transformation, coordinate mapping, and progressive reveal.

Manim visualizations are particularly effective for:
- Showing state transformations (before/after comparisons)
- Demonstrating coordinate/index mapping with arrows
- Color-coding elements to track movement through algorithms
- Animating step-by-step processes with intermediate states
- Including formulas and mathematical explanations inline

## When to Use

Use this skill when you need to:
- Create visual explanations for algorithm operations
- Demonstrate data structure transformations
- Animate coordinate transformation formulas
- Build educational content showing step-by-step processes
- Create interview preparation materials with visual aids
- Illustrate complex algorithmic logic that benefits from animation

## Visualization Architecture

A complete Manim visualization consists of three components:

### 1. **Visualization Scene** (`operation_viz.py`)
The main Manim Scene subclass that defines the animation logic.

### 2. **Runner Script** (`operation_viz_example.py`)
A standalone script that executes the visualization and saves output.

### 3. **Supporting Documentation**
Header notes and comments explaining the visualization strategy.

---

## Header Structure for Visualization Files

A visualization file header should include:

```python
"""
## Operation Overview

[1-2 sentence description of what operation is being visualized]

Shows the step-by-step transformation using [algorithm/formula]:
[Key formula or mathematical concept]

Example with concrete values:
[Before state example]
[After state example]

Visualizes:
1. [Element 1 of visualization]
2. [Element 2 of visualization]
3. [Element 3 of visualization]
"""
```

---

## Step-by-Step Implementation Guide

### 1. Operation Overview Section
**What to include:**
- Clear description of the operation being visualized (1-2 sentences)
- The algorithm or mathematical formula involved
- Concrete example with input and output
- Bulleted list of what the visualization shows (3-5 key elements)

**Example:**
```
Visualization of the 90-degree clockwise matrix rotation algorithm.

Shows the step-by-step transformation using the coordinate transformation formula:
rotated[c][rows - 1 - r] = matrix[r][c]

Uses a 3×3 matrix example:
Original: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Rotated:  [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

Visualizes:
1. Original matrix on the left
2. Empty rotated matrix on the right
3. Element-by-element transformation with arrows
4. Color-coded elements to track movement
5. Transformation formula displayed during animation
```

### 2. Visualization Strategy Section
**What to include:**
- How data is represented visually (shapes, colors, layout)
- The animation flow (what happens in sequence)
- Color scheme and what each color represents
- Positioning strategy (left/right/center layout)

**Template:**
```python
# Scene Layout Strategy
# - [Where element A goes] → [Why this placement]
# - [Where element B goes] → [Why this placement]
# - [Where element C goes] → [Why this placement]

# Color Scheme
# - [Color 1]: [Meaning]
# - [Color 2]: [Meaning]
# - [Color 3]: [Meaning]

# Animation Flow
# 1. [Initial state display] (timing: X seconds)
# 2. [Transformation step] (timing: X seconds)
# 3. [Result display] (timing: X seconds)
```

### 3. Key Visualization Concepts Section
**What to include:**
- 2-3 critical design decisions in the visualization
- For each: WHY was this choice made and HOW does it help understanding
- Trade-offs (e.g., complexity vs. clarity)

**Template for each concept:**
```
- [Visualization technique/choice]
[Why is this important? What understanding does it enable?]
[How is it implemented? Any constraints?]
```

**Example:**
```
- Why show both matrices side-by-side?
Parallel layout allows viewers to simultaneously see source and destination,
making the coordinate transformation mapping immediately intuitive.
Implemented with LEFT positioning for original, RIGHT for rotated.

- Why color-code each element?
Color persistence through the animation tracks individual element movement,
helping viewers understand which original position maps to which new position.
Implemented with a color palette that cycles through distinct colors.

- Why show arrows between matrices?
Arrows make the coordinate mapping explicit, showing the exact transformation
path from source to destination. This reinforces the mathematical formula.
Implemented with Create animation for emphasis, FadeOut to avoid clutter.
```

### 4. Animation Flow Section
**What to include:**
- Sequence of animation steps
- Timing for each major phase
- What user sees at each stage
- State transitions (e.g., when formulas appear/disappear)

**Template:**
```
Animation Sequence:
1. Title and formula display (0.5s write + 0.5s wait)
2. Original matrix creation (parallel Create for boxes and text)
3. Rotated matrix skeleton (empty boxes, indicates dimensions)
4. Element-by-element transformation loop:
   - Highlight source element (Indicate with color)
   - Display current formula (Write with current indices)
   - Draw arrow to destination (Create Arrow)
   - Update destination element (FadeIn text)
   - Clear temporary elements (FadeOut formula and arrow)
5. Final summary (completion message + complexity info)
```

### 5. Implementation Notes Section
**What to include:**
- Key technical decisions in code
- How to calculate positions and indices
- Handling of flat vs. multi-dimensional data
- Color palette and animation timing choices

**Example:**
```
Technical Implementation Notes:

Position Calculation:
- Matrix elements positioned using: ORIGIN + direction * base + RIGHT * (c * spacing) + DOWN * (r * spacing)
- Spacing of 0.8 units ensures clear visual separation
- Base offsets (LEFT*3, RIGHT*3) center matrices on screen

Index Management:
- Flattened index = r * cols + c (for accessing VGroup items)
- Original position: [r][c], Transformed position: [c][rows - 1 - r]
- Indices displayed in real-time formula updates

Color Palette:
- 9-color cycle to distinguish all elements in 3x3 matrix
- Same color maintained throughout transformation to track movement
- Provides visual feedback when elements arrive at destination

Animation Timing:
- Source highlight: Indicate() with 1.2 scale factor
- Arrow creation: 0.3s default
- Element arrival: FadeIn with simultaneous Indicate highlight
```

### 6. Multiple Summary Formats

**30-Second Pitch:**
Natural, verbal explanation suitable for quick communication:
```
"This visualization shows how a matrix is rotated 90 degrees clockwise
using a coordinate transformation formula. Each element from the original
matrix is mapped to its new position through the formula rotated[c][rows-1-r] = matrix[r][c].
The animation displays each mapping step-by-step with arrows and color-coding,
making the pattern clear and the formula intuitive."
```

**Rapid-Fire Version:**
Bullet points capturing key technical points:
```
- Shows 90-degree clockwise matrix rotation step-by-step
- Uses coordinate transformation: rotated[c][rows-1-r] = matrix[r][c]
- Color-codes elements to track movement through algorithm
- Displays transformation formulas in real-time
- Shows both original (3×3) and rotated (3×3) matrices side-by-side
- Time: O(n×m), Space: O(n×m), Non-mutating algorithm
```

**Ultra-Minimal One-Liner:**
Single sentence capturing the essence:
```
"Step-by-step animation of matrix rotation showing coordinate mapping
from original to rotated position for each element."
```

---

## Manim Fundamentals for Visualization

### Core Imports
```python
from manim import (
    # Colors
    BLUE, RED, GREEN, YELLOW, WHITE,
    # Directions
    UP, DOWN, LEFT, RIGHT, ORIGIN,
    # Shapes
    Rectangle, VGroup,
    # Animations
    Create, FadeIn, FadeOut, Write, Indicate,
    # Special
    Arrow, Text, Scene,
)
```

### Common Patterns

**Creating a grid of elements:**
```python
elements = VGroup()
for r in range(rows):
    for c in range(cols):
        element = Rectangle(width=0.6, height=0.6)
        element.move_to(ORIGIN + RIGHT*(c*0.8) + DOWN*(r*0.8))
        elements.add(element)
```

**Animating transformations:**
```python
# Highlight source
self.play(Indicate(source, color=color, scale_factor=1.2))

# Show arrow with transformation
arrow = Arrow(source.get_center(), dest.get_center())
self.play(Create(arrow))

# Update destination and highlight
self.play(FadeIn(dest_text), Indicate(dest, color=color))

# Clean up temporary elements
self.play(FadeOut(arrow), FadeOut(temp_text))
```

**Positioning elements:**
```python
# Position relative to screen edges
element.to_edge(LEFT)  # Far left
element.to_edge(RIGHT)  # Far right
element.to_edge(UP)     # Top
element.to_edge(DOWN)   # Bottom

# Position relative to other elements
element.next_to(other, DOWN, buff=0.3)  # Below, with 0.3 unit gap

# Absolute positioning
element.move_to(ORIGIN + RIGHT*3 + DOWN*2)
```

---

## Quality Checklist

Before finalizing a visualization, verify:

- [ ] **Operation Overview** clearly describes what's being visualized
- [ ] **Visualization Strategy** explains layout, colors, and flow
- [ ] **Key Concepts** explain WHY each design choice improves understanding
- [ ] **Animation Flow** sequences steps with appropriate timing
- [ ] **Implementation Notes** document technical decisions
- [ ] **30-Second Pitch** is natural and conversational
- [ ] **Rapid-Fire Version** uses clear bullet points
- [ ] **Ultra-Minimal One-Liner** captures essence in one sentence
- [ ] **Animations are paced** appropriately (not too fast, not too slow)
- [ ] **Color scheme** provides good contrast and distinguishes elements
- [ ] **Formulas/text** are readable (appropriate font sizes)
- [ ] **Scene layout** utilizes screen space effectively
- [ ] **Runner script** properly executes the visualization
- [ ] All necessary Manim imports are included
- [ ] Position calculations avoid overlapping elements

---

## File Structure Template

```
drills/visualizations/
├── operation_viz.py                    # Main Scene class
└── operation_viz_example.py (optional) # Runner script
```

### operation_viz.py Template
```python
"""
## Operation Overview

[Description of the operation]

[Concrete example]

Visualizes:
1. [Element 1]
2. [Element 2]
"""

from manim import (
    # ... imports
)

class OperationVisualization(Scene):
    """
    Visualization of [operation name].

    [Detailed docstring describing what happens]
    """

    def construct(self):
        # Title and setup
        # Element creation
        # Animation loop
        # Summary
```

### operation_viz_example.py Template
```python
#!/usr/bin/env python
"""
Runner script for operation_viz.py visualization.

This script renders the [operation] visualization using [formula/concept].
"""

import subprocess
import sys
from pathlib import Path

def run_visualization():
    """Run the visualization using manim."""
    script_dir = Path(__file__).parent
    viz_script = script_dir / "operation_viz.py"
    media_dir = script_dir.parent.parent / "generated" / "media"

    media_dir.mkdir(parents=True, exist_ok=True)

    cmd = [
        "manim",
        "-qh",  # high quality
        "-p",   # preview
        "--media_dir", str(media_dir),
        str(viz_script),
        "OperationVisualization",
    ]

    try:
        result = subprocess.run(cmd, check=True, capture_output=False)
        print(f"SUCCESS: Visualization rendered to {media_dir}")
        return result.returncode
    except subprocess.CalledProcessError as e:
        print(f"ERROR: Failed rendering visualization: {e}")
        return 1
    except FileNotFoundError:
        print("ERROR: Manim not found. Install with: pip install manim")
        return 1

if __name__ == "__main__":
    sys.exit(run_visualization())
```

---

## Common Pitfalls to Avoid

❌ **Too fast animations:** Viewers can't follow the logic
→ ✅ Add `self.wait()` between major steps; use slower animations for important transitions

❌ **Poor color contrast:** Elements blend together
→ ✅ Use distinct colors; test with colorblind-friendly palettes

❌ **Cluttered layout:** Too much happening simultaneously
→ ✅ Use FadeOut to clean up temporary elements; space items clearly

❌ **Missing context:** Formula shown without explanation
→ ✅ Display current step information; update formulas to show actual indices

❌ **Unreadable text:** Font size too small or positioned poorly
→ ✅ Use font_size >= 18 for text; position with next_to() or move_to()

❌ **Arbitrary positioning:** Elements scattered randomly
→ ✅ Use consistent spacing; align elements in grids or rows

---

## Tags

`#visualization` `#manim` `#animation` `#algorithm-explanation` `#educational` `#interview-prep` `#step-by-step` `#mathematical-animation` `#skill`
