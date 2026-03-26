"""
Example usage of the N-Queens visualization.

This script demonstrates different ways to use the N-Queens solver and renderer.
"""

from .algos import solve_n_queens_visual
from .render import NQueensRenderer


def example_basic():
    """Basic example: Solve and visualize 4-Queens with dark theme."""
    print("Starting 4-Queens visualization with dark theme...")
    renderer = NQueensRenderer(n=4, theme='dark', cell_size=100)
    event_generator = solve_n_queens_visual(4)
    renderer.render(event_generator)


def example_light_theme():
    """Example with light theme."""
    print("Starting 6-Queens visualization with light theme...")
    renderer = NQueensRenderer(n=6, theme='light', cell_size=80)
    event_generator = solve_n_queens_visual(6)
    renderer.render(event_generator)


def example_large_board():
    """Example with larger board."""
    print("Starting 8-Queens visualization...")
    renderer = NQueensRenderer(n=8, theme='dark', cell_size=70)
    event_generator = solve_n_queens_visual(8)
    renderer.render(event_generator)


def example_analyze_events():
    """Example: Analyze algorithm events without rendering."""
    print("\nAnalyzing algorithm events for 4-Queens:")
    print("-" * 50)

    events = list(solve_n_queens_visual(4))

    # Categorize events
    event_counts = {}
    solutions = []

    for event in events:
        event_type = event[0]
        event_counts[event_type] = event_counts.get(event_type, 0) + 1

        if event_type == 'solution':
            solutions.append(event[1])

    # Print analysis
    print(f"Total events: {len(events)}")
    for event_type, count in sorted(event_counts.items()):
        print(f"  {event_type}: {count}")

    print(f"\nFound {len(solutions)} solution(s):")
    for i, solution in enumerate(solutions, 1):
        print(f"\nSolution {i}:")
        for row in solution:
            print(''.join(row))


if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Usage: python example.py [basic|light|large|analyze]")
        print("\nRunning basic example by default...")
        example_basic()
    else:
        mode = sys.argv[1].lower()
        if mode == 'basic':
            example_basic()
        elif mode == 'light':
            example_light_theme()
        elif mode == 'large':
            example_large_board()
        elif mode == 'analyze':
            example_analyze_events()
        else:
            print(f"Unknown mode: {mode}")
            print("Valid modes: basic, light, large, analyze")
