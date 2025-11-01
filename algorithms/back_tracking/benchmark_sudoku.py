import statistics
import time
from copy import deepcopy

from algorithms.back_tracking.sudoku_solver import solve_sudoku as solver1
from algorithms.back_tracking.sudoku_solver_alt import solve_sudoku as solver2

SAMPLE_BOARD = [
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

def benchmark_solver(solver, board, trials=5):
    durations = []
    for _ in range(trials):
        test_board = deepcopy(board)
        start = time.time()
        solver(test_board)
        end = time.time()
        durations.append(end - start)
    return {
        "average": statistics.mean(durations),
        "min": min(durations),
        "max": max(durations),
        "all": durations
    }

def run_benchmark(trials=5):
    print(f"Benchmarking Sudoku solvers over {trials} trials...\n")

    print("Running Solver 1 (Backtracking)...")
    stats1 = benchmark_solver(solver1, SAMPLE_BOARD, trials)

    print("Running Solver 2 (Alternative)...")
    stats2 = benchmark_solver(solver2, SAMPLE_BOARD, trials)

    print("\n📊 Results:")
    print(f"{'Solver':<25} {'Avg Time':<10} {'Min':<10} {'Max':<10}")
    print(f"{'Backtracking':<25} {stats1['average']:.5f}  {stats1['min']:.5f}  {stats1['max']:.5f}")
    print(f"{'Alternative':<25} {stats2['average']:.5f}  {stats2['min']:.5f}  {stats2['max']:.5f}")

if __name__ == "__main__":
    run_benchmark()
