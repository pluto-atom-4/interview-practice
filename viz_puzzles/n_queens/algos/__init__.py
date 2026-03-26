"""N-Queens solving algorithms with event yielding for visualization."""


def solve_n_queens_visual(n: int):
    """
    Solve N-Queens using backtracking, yielding events for visualization.

    Yields events with format:
    - ('place', row, col): Place a queen
    - ('check', row, col): Checking if a cell is valid
    - ('remove', row, col): Remove a queen (backtrack)
    - ('solution', board): Valid solution found
    """
    results = []
    board = [['.' for _ in range(n)] for _ in range(n)]
    cols = set()
    pos_diag = set()
    neg_diag = set()

    def backtrack(r):
        if r == n:
            # Found a solution
            solution = [['Q' if cell == 'Q' else '.' for cell in row] for row in board]
            results.append(solution)
            yield ('solution', [row[:] for row in solution])
            return

        for c in range(n):
            # Check if placement is valid
            yield ('check', r, c)

            if c in cols or (r + c) in pos_diag or (r - c) in neg_diag:
                continue

            # Place queen
            board[r][c] = 'Q'
            cols.add(c)
            pos_diag.add(r + c)
            neg_diag.add(r - c)
            yield ('place', r, c)

            # Recurse
            yield from backtrack(r + 1)

            # Backtrack
            board[r][c] = '.'
            cols.remove(c)
            pos_diag.remove(r + c)
            neg_diag.remove(r - c)
            yield ('remove', r, c)

    yield from backtrack(0)
    return results
