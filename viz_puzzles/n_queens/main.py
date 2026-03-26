"""Main entry point for N-Queens visualization."""

import sys
import os

# Add project root to path for direct script execution
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from viz_puzzles.n_queens.algos import solve_n_queens_visual
from viz_puzzles.n_queens.render import NQueensRenderer


def main():
    """
    Run the N-Queens visualization.
    Accepts command-line arguments: n-queens-viz [SIZE] [THEME]
    """
    n = None
    theme = 'dark'

    # Parse command line arguments
    if len(sys.argv) > 1:
        try:
            n = int(sys.argv[1])
        except ValueError:
            pass

    if len(sys.argv) > 2:
        theme = sys.argv[2]

    # Prompt for board size if not provided
    if n is None:
        try:
            n = int(input("Enter board size (1-9): "))
        except (ValueError, EOFError):
            print("Invalid input. Using N=4.")
            n = 4

    if not 1 <= n <= 9:
        print(f"Board size must be 1-9, got {n}. Using N=4.")
        n = 4

    print(f"Starting N-Queens visualization with N={n}")
    print("Controls:")
    print("  SPACE: Pause/Resume animation")
    print("  LEFT/RIGHT: Navigate between solutions")
    print("  CLOSE WINDOW: Exit")

    # Create renderer and run visualization
    renderer = NQueensRenderer(n, theme=theme)
    event_generator = solve_n_queens_visual(n)
    renderer.render(event_generator)


if __name__ == '__main__':
    main()
