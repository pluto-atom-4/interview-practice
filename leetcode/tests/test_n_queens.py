import pytest


from leetcode.n_queens import solve_n_queens


def normalize(solutions):
    """Sort solutions for order‑independent comparison."""
    return sorted([tuple(sol) for sol in solutions])

def test_n_queens_n1():
    assert solve_n_queens(1) == [["Q"]]

def test_n_queens_n4():
    expected = [
        [
            ".Q..",
            "...Q",
            "Q...",
            "..Q.",
        ],
        [
            "..Q.",
            "Q...",
            "...Q",
            ".Q..",
        ],
    ]
    result = solve_n_queens(4)
    assert normalize(result) == normalize(expected)