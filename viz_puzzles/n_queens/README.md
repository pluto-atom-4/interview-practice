# N-Queens Puzzle Visualization

A pygame-based interactive visualization of the N-Queens puzzle solving algorithm using backtracking. Watch in real-time as the algorithm explores the solution space, places and removes queens, and discovers all valid solutions.

## Features

- **Interactive Visualization**: Watch the backtracking algorithm solve N-Queens in real-time
- **Event-Driven Animation**: Visualize each step: checking cells, placing queens, and backtracking
- **Multiple Solutions**: Automatically finds and displays all valid solutions
- **Theme Support**: Light and dark color themes
- **Responsive Controls**:
  - **SPACE**: Pause/Resume animation
  - **LEFT/RIGHT**: Navigate between solutions
  - **Close Window**: Exit

## Architecture Flow

```
main.py
  ├─ Parses CLI arguments
  ├─ Prompts user for N
  └─ Creates: NQueensRenderer(n, theme)
        └─ solve_n_queens_visual(n) [generator]
              ├─ Yields: check, place, remove events
              └─ Yields: solution events
        
Renderer.render(event_generator)
  ├─ Main pygame loop (60 FPS)
  ├─ Consumes events from generator (50ms interval)
  ├─ Updates board state
  └─ Renders visual representation
```


## Quick Start

### CLI Entry Point (Easiest)

Once installed, use the `n-queens-viz` command:

```bash
n-queens-viz              # Prompts for board size
n-queens-viz 4            # 4-Queens with dark theme (default)
n-queens-viz 8 light      # 8-Queens with light theme
```

### Python Module

```bash
python -m viz_puzzles.n_queens.main 4
python -m viz_puzzles.n_queens.main    # Interactive mode
```

### As a Python Library

```python
from viz_puzzles.n_queens.main import main

main()  # Prompts for input
```

## Installation

The visualization is included in this project. Ensure the package is installed:

```bash
uv pip install -e .  # Recommended (uses uv for fast dependency management)
# or
pip install -e .
```

Both pygame and the package dependencies will be installed automatically.

## How It Works

### Algorithm: Backtracking with Constraint Tracking

The N-Queens solver uses **backtracking** with efficient constraint checking:

1. **Row-by-Row Placement**: Place one queen per row (enforces row constraint automatically)
2. **Column Checking**: Track occupied columns in a set (O(1) lookup)
3. **Diagonal Checking**: Track both diagonals using two sets (positive: r-c, negative: r+c)
4. **Recursive Exploration**: Try each column; if valid, place queen and recurse
5. **Backtracking**: Undo placement and try next column when stuck

**Time Complexity**: O(N!) - explores all valid placements
**Space Complexity**: O(N²) - board storage, O(N) recursion depth, O(N) constraint sets

### Event-Based Rendering

The algorithm is generator-based, yielding events for smooth animation:

| Event | Meaning |
|-------|---------|
| `check (r, c)` | Evaluating if cell (r, c) can have a queen |
| `place (r, c)` | Successfully placed a queen at (r, c) |
| `remove (r, c)` | Removed a queen during backtracking |
| `solution (board)` | Found a complete valid solution |

The renderer processes these events frame-by-frame, creating a visual narrative of the solving process.

### Visual Elements

- **Board**: N×N chessboard with alternating colors
- **Queens**: Gold circles (dark theme) or orange circles (light theme)
- **Checking Highlight**: Red overlay on cells being evaluated
- **Row Indicator**: Displays current row being processed

## Expected Solutions

Known solution counts for N-Queens:
- N=1: 1 solution
- N=2: 0 solutions
- N=3: 0 solutions
- N=4: 2 solutions
- N=5: 10 solutions
- N=6: 4 solutions
- N=7: 40 solutions
- N=8: 92 solutions
- N=9: 352 solutions

## Implementation Details

### Directory Structure

```
viz_puzzles/n_queens/
├── main.py              # CLI entry point (accepts args: SIZE [THEME])
├── render.py            # Pygame visualization renderer
├── config.py            # Color theme definitions (dark/light)
├── algos/
│   └── __init__.py      # Event-yielding N-Queens backtracking solver
├── example.py           # Usage examples (basic, light, large, analyze)
├── test_solver.py       # Algorithm verification tests
└── README.md            # This file
```

### Color Themes

#### Dark Theme (Default)
- **Background**: Dark gray (30, 30, 30)
- **Board**: Gray and darker gray squares
- **Queens**: Gold circles with dark border
- **Checking**: Red overlay on evaluated cells
- **Text**: White on dark background

#### Light Theme
- **Background**: Light gray (240, 240, 240)
- **Board**: Brown and tan squares (traditional chessboard)
- **Queens**: Orange circles with dark border
- **Checking**: Light red overlay
- **Text**: Dark on light background

### Configuration

Modify animation behavior in `render.py`:

```python
class NQueensRenderer:
    def __init__(self, n, theme='dark', cell_size=80):
        self.event_delay = 50  # ms between events (default: 50)
        self.clock.tick(60)    # FPS (default: 60)
```

## Performance & Optimization

| Aspect | Value |
|--------|-------|
| Animation Frame Rate | 60 FPS |
| Event Processing | 50ms (adjustable) |
| Board Sizes Supported | 1–9 (≤ 352 solutions) |
| Solver Speed | O(N!) - very fast for N ≤ 9 |
| Memory Usage | O(N²) - minimal for small boards |
| Rendering | Real-time event streaming |

## Keyboard Controls

| Key | Action |
|-----|--------|
| **SPACE** | Pause/Resume animation |
| **LEFT** | Previous solution (after complete) |
| **RIGHT** | Next solution (after complete) |
| **CLOSE WINDOW** | Exit program |

## Troubleshooting

### No Display Available (Headless Environment)

If running on a server or headless system, verify the algorithm works without GUI:

```bash
python -m viz_puzzles.n_queens.test_solver
```

This script tests the solver and prints all solutions for N=1 through N=8 without requiring a display.

Expected output:
```
Testing 4-Queens solver:
Events generated: 94
  Placements: 16
  Removals: 16
  Checks: 60
  Solutions found: 2
```

### ImportError with Relative Imports

Always run using the `-m` flag to ensure proper module resolution:

```bash
python -m viz_puzzles.n_queens.main 4
# ✓ Correct

python viz_puzzles/n_queens/main.py
# ✗ Will fail (relative import error)
```

Or use the CLI entry point:

```bash
n-queens-viz 4
# ✓ Always works (after installation)
```

### Slow or Fast Animation

Adjust animation speed by modifying `event_delay` in `render.py` (line ~51):

```python
self.event_delay = 50  # Default: 50ms between events
# Faster:  10-30ms
# Slower:  100-200ms
```

### Window Won't Close

If the pygame window becomes unresponsive:

- Press **SPACE** to ensure it's not frozen
- Force quit: **Ctrl+C** in the terminal, or close from window manager

### Memory Issues with Large Boards

The solver supports N=1–9 efficiently. For N≥10, expect:
- Exponentially longer computation (O(N!) complexity)
- Thousands of intermediate states
- Hundreds of solutions

Not recommended without significant optimization.

## Examples

### Example Scripts

The `example.py` file contains multiple usage examples:

```bash
# Basic 4-Queens visualization
python -m viz_puzzles.n_queens.example basic

# Light theme with 6-Queens
python -m viz_puzzles.n_queens.example light

# Large board (8-Queens)
python -m viz_puzzles.n_queens.example large

# Analyze algorithm events without rendering
python -m viz_puzzles.n_queens.example analyze
```

### Programmatic Usage

Integrate the solver into your own code:

```python
from viz_puzzles.n_queens.algos import solve_n_queens_visual
from viz_puzzles.n_queens.render import NQueensRenderer

# Method 1: Full visualization
renderer = NQueensRenderer(n=5, theme='dark', cell_size=100)
events = solve_n_queens_visual(5)
renderer.render(events)

# Method 2: Analyze events without rendering
events = list(solve_n_queens_visual(4))
solutions = [e[1] for e in events if e[0] == 'solution']
print(f"Found {len(solutions)} solutions")

# Method 3: Get just the solutions
from leetcode.n_queens import solve_n_queens
solutions = solve_n_queens(4)  # Returns all solutions directly
```

## Advanced Usage

### Custom Renderer Configuration

```python
from viz_puzzles.n_queens.render import NQueensRenderer
from viz_puzzles.n_queens.algos import solve_n_queens_visual

renderer = NQueensRenderer(
    n=6,
    theme='light',           # 'dark' or 'light'
    cell_size=100            # Larger cells = bigger window
)

# Optionally modify animation speed
renderer.event_delay = 20    # Faster animation (20ms per event)

# Run visualization
renderer.render(solve_n_queens_visual(6))
```

### Custom Themes

Define your own theme in `config.py`:

```python
from dataclasses import dataclass
from viz_puzzles.n_queens.config import Theme

CUSTOM_THEME = Theme(
    background=(20, 20, 40),          # Dark blue
    board_dark=(60, 60, 100),
    board_light=(100, 100, 150),
    queen=(255, 255, 0),              # Yellow
    queen_border=(200, 200, 0),
    checking=(255, 100, 100),
    valid=(100, 255, 100),
    invalid=(255, 100, 100),
    text=(200, 200, 200),
    grid_border=(150, 150, 200),
)

# Then register and use it
THEMES['custom'] = CUSTOM_THEME
renderer = NQueensRenderer(n=4, theme='custom')
```

### Extracting Event Data

Process algorithm events without visualization:

```python
from viz_puzzles.n_queens.algos import solve_n_queens_visual

events = list(solve_n_queens_visual(4))

# Count event types
from collections import Counter
event_types = Counter(e[0] for e in events)
print(event_types)  # Counter({'check': 60, 'place': 16, 'remove': 16, 'solution': 2})

# Extract all solutions
solutions = [e[1] for e in events if e[0] == 'solution']
for i, sol in enumerate(solutions, 1):
    print(f"Solution {i}:")
    for row in sol:
        print(''.join(row))
```

## Testing

Verify the implementation with the built-in test suite:

```bash
# Test algorithm correctness
python -m viz_puzzles.n_queens.test_solver

# Run project tests (if configured)
pytest tests/
```

Expected solution counts (verified):
- N=1: 1 | N=2: 0 | N=3: 0 | N=4: 2 | N=5: 10
- N=6: 4 | N=7: 40 | N=8: 92 | N=9: 352

## References

- **N-Queens Problem**: [Wikipedia](https://en.wikipedia.org/wiki/Eight_queens_puzzle)
- **Backtracking Algorithm**: [GeeksforGeeks](https://www.geeksforgeeks.org/n-queen-problem-backtracking-using-bit-manipulation/)
- **Pygame Documentation**: [pygame.org](https://www.pygame.org/docs/)

## License

Part of the interview-practice repository.
