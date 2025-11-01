from algorithms.back_tracking.benchmark_sudoku import benchmark_solver
from algorithms.back_tracking.sudoku_solver import solve_sudoku as solver1
from algorithms.back_tracking.sudoku_solver_alt import solve_sudoku as solver2


def test_benchmark_solvers():
    board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    stats1 = benchmark_solver(solver1, board, trials=2)
    stats2 = benchmark_solver(solver2, board, trials=2)
    assert stats1["average"] > 0
    assert stats2["average"] > 0
