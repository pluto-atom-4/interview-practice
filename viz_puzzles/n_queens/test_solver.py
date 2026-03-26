"""Test script to verify the N-Queens solver without GUI."""

from .algos import solve_n_queens_visual


def test_solver(n: int):
    """Test the solver and print event log."""
    print(f"\nTesting {n}-Queens solver:")
    print("-" * 50)

    events = list(solve_n_queens_visual(n))

    # Count events
    placements = sum(1 for e in events if e[0] == 'place')
    removals = sum(1 for e in events if e[0] == 'remove')
    checks = sum(1 for e in events if e[0] == 'check')
    solutions = sum(1 for e in events if e[0] == 'solution')

    print(f"Events generated: {len(events)}")
    print(f"  Placements: {placements}")
    print(f"  Removals: {removals}")
    print(f"  Checks: {checks}")
    print(f"  Solutions found: {solutions}")

    # Extract and print solutions
    for event in events:
        if event[0] == 'solution':
            print("\nSolution found:")
            board = event[1]
            for row in board:
                print(''.join(row))

    return solutions


if __name__ == '__main__':
    for n in range(1, 9):
        count = test_solver(n)
        expected = {1: 1, 2: 0, 3: 0, 4: 2, 5: 10, 6: 4, 7: 40, 8: 92}
        print(f"Expected: {expected.get(n, '?')}, Got: {count}")
