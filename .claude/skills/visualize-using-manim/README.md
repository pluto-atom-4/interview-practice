# Visualize Using Manim Skill - Usage Guide

## Quick Start

This skill helps you create step-by-step algorithm visualizations using Manim. It provides guidance on:
- Structuring animation scenes for maximum clarity
- Designing effective visual representations
- Organizing files and runner scripts
- Documenting visualizations with multiple explanation formats

## Prerequisites

Before using this skill, ensure you have Manim installed:
```bash
pip install manim
```

For best results, also install:
```bash
pip install pillow
```

## Usage in Claude Code Agent

### Invoking the Skill

You can invoke this skill within Claude Code in two ways:

1. **Using the Skill Command:**
   ```
   /visualize-using-manim
   ```
   Claude Code will prompt for the operation you want to visualize.

2. **Direct Skill Invocation:**
   ```
   skill: "visualize-using-manim", args: "matrix_rotation"
   ```
   Directly specifies which operation to create a visualization for.

### Workflow Integration

**Step 1: Identify the Operation**
- Choose an algorithm or data structure operation you want to visualize
- Examples: matrix rotation, array transformation, linked list traversal, tree traversal
- Identify the key insight or transformation to highlight

**Step 2: Plan the Visualization Strategy**
- What are the input and output states?
- How will you represent data visually (boxes, circles, arrays)?
- What is the transformation path or formula?
- What colors and animations would make it clear?

**Step 3: Create the Visualization Files**
- Create `operation_viz.py` with the Scene class
- Create `operation_viz_example.py` as the runner script
- Use the templates from SKILL.md as your starting point

**Step 4: Add Documentation Header**
- Include the Operation Overview section
- Document the visualization strategy
- Explain key design concepts
- Provide multiple summary formats

**Step 5: Test and Refine**
- Run the visualization: `python operation_viz_example.py`
- Check animation timing (is it too fast? too slow?)
- Verify colors and layout (is everything readable?)
- Adjust animations and wait times as needed

**Step 6: Refine Based on Feedback**
- Re-run after making changes
- Update documentation if you change the visualization approach
- Ensure all code comments match what the animation actually shows

### Example Workflow

```bash
# Create visualization files for matrix rotation
# Files created:
# - drills/visualizations/rotate_matrix_viz.py
# - drills/visualizations/rotate_matrix_viz_example.py

# Run the visualization
cd drills/visualizations
python rotate_matrix_viz_example.py

# Result: Animation opens showing step-by-step matrix rotation

# If you want to modify the visualization:
# - Edit rotate_matrix_viz.py to change animation logic
# - Edit rotate_matrix_viz_example.py if you need different manim flags
# - Re-run the runner script to see changes
```

## File Structure

After using this skill, your project structure should look like:

```
drills/ 
├── visualizations/ 
│    ├── operation_viz.py # Main animation Scene 
│    └── operation_viz_example.py # Runner script
generated/ 
└── media/ 
     └── videos/ # Output files
```

## Tips for Best Results

### Animation Pacing
- Use `self.wait(0.5)` between major sections to give viewers time to process
- Keep most animations under 0.3-0.5 seconds; use longer times only for emphasis
- Balance speed: information should be clear but presentation engaging

### Visual Clarity
- Use high contrast colors (BLUE, RED, GREEN, YELLOW)
- Avoid color combinations that are hard to distinguish
- Text should be at least font_size=18 for readability
- Use color consistently: same color = same logical element

### Layout Strategy
- Position related elements close together
- Use alignment (to_edge, next_to) rather than arbitrary positioning
- Leave 0.3-0.5 unit gaps between elements for breathing room
- Center main content on screen

### Documentation
- Update the header whenever you significantly change the animation
- Include both high-level and technical documentation
- Provide multiple explanation formats (pitch, rapid-fire, one-liner)
- Document WHY you made visualization design choices

### Testing
- Run visualization with `-qh` flag for high quality during final export
- Use `-ql` (low quality) for quick testing while developing
- Verify all animations play smoothly without visual glitches
- Check that formulas and text remain readable throughout

## Running Visualizations

### Standard Execution
```bash
python operation_viz_example.py
```
This renders the visualization in high quality and opens it in your default player.

### Custom Manim Flags
Edit the runner script to change quality or output options:

```python
cmd = [
    "manim",
    "-ql",      # Low quality (faster)
    "-qm",      # Medium quality
    "-qh",      # High quality (default, slower)
    "-p",       # Preview (open after rendering)
    "-s",       # Save as .png instead of .mp4
    "--media_dir", str(media_dir),
    str(viz_script),
    "SceneClassName",
]
```

## Common Scene Structure

Most visualizations follow this pattern:

```python
def construct(self):
    # 1. Title and introduction (0.5-1s)
    title = Text("Operation Name", font_size=36).to_edge(UP)
    self.play(Write(title))
    self.wait(0.5)

    # 2. Setup data and display initial state (1-2s)
    data = [1, 2, 3, 4, 5]
    # Create visual representations
    self.play(Create(visual_elements))
    self.wait(1)

    # 3. Step-by-step transformation (varies)
    for step in transformation_steps:
        # Highlight source
        # Show transformation
        # Update destination
        # Clean up temporary elements
        self.wait(0.3)

    # 4. Summary (0.5-1s)
    summary = Text("Complete!", font_size=24)
    self.play(Write(summary))
    self.wait(1)
```

## Integration with Interview Prep

Use visualizations as part of your interview preparation:

1. **Communication Tool:** Recreate the visualization verbally during interviews
2. **Understanding:** Explain what each animation phase shows
3. **Confidence:** Review visualizations before interviews to reinforce understanding
4. **Teaching:** Share visualizations when explaining algorithms to others

Refer to the **30-Second Pitch** from your visualization header when explaining verbally.

## Troubleshooting

### Manim Not Found
```
ERROR: Manim not found. Install with: pip install manim
```
**Solution:** Install Manim using pip: `pip install manim`

### Slow Rendering
**Problem:** Visualization takes too long to render
**Solution:** Use `-ql` flag for testing: modify runner script to use `-ql` during development

### Visual Glitches
**Problem:** Elements overlap or positioning looks wrong
**Solution:** Check position calculations; use next_to() and alignment methods for consistent spacing

### Animations Too Fast
**Problem:** Can't follow what's happening
**Solution:** Add more `self.wait()` calls; reduce animation duration in play() calls

## Examples in the Codebase

Check these example visualizations for reference:

- `drills/visualizations/rotate_matrix_viz.py` - Matrix rotation with coordinate mapping
- `drills/visualizations/rotate_matrix_viz_example.py` - Example runner script pattern

## Next Steps

1. **Start with a simple operation:** Begin with a single-step transformation
2. **Build complexity gradually:** Add more steps as you become comfortable
3. **Document thoroughly:** Include all header sections from SKILL.md
4. **Iterate:** Run frequently to see changes in real-time
5. **Share:** Use visualizations in presentations or documentation

---

For complete documentation including implementation guide, quality checklist, and technical details, see [SKILL.md](SKILL.md).
