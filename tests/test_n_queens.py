import pytest

from algorithms.back_tracking.n_queens import format_solution, solve_n_queens


def test_n_queens_4():
    solutions = solve_n_queens(4)
    assert len(solutions) == 2
    formatted = [format_solution(sol) for sol in solutions]
    for sol in formatted:
        assert all("Q" in row for row in sol)
        assert len(sol) == 4


def test_n_queens_1():
    solutions = solve_n_queens(1)
    assert len(solutions) == 1
    assert format_solution(solutions[0]) == ["Q"]


def test_n_queens_2_and_3():
    assert solve_n_queens(2) == []
    assert solve_n_queens(3) == []
