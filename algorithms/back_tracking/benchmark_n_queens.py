import statistics
import time

from n_queens import solve_n_queens
from n_queens_alt import n_queens  # Your optimized version


def benchmark(func, n, trials=5):
    durations = []
    for _ in range(trials):
        start = time.time()
        func(n)
        end = time.time()
        durations.append(end - start)
    return {
        "average": statistics.mean(durations),
        "min": min(durations),
        "max": max(durations),
        "all": durations,
    }


def run_benchmark(n=8, trials=5):
    print(f"Benchmarking N-Queens with n={n} over {trials} trials...\n")

    print("Running original version (solve_n_queens)...")
    original_stats = benchmark(solve_n_queens, n, trials)

    print("Running optimized version (n_queens)...")
    optimized_stats = benchmark(n_queens, n, trials)

    print("\n📊 Results:")
    print(f"{'Version':<20} {'Avg Time':<10} {'Min':<10} {'Max':<10}")
    print(
        f"{'Original':<20} {original_stats['average']:.5f}  {original_stats['min']:.5f}  {original_stats['max']:.5f}"
    )
    print(
        f"{'Optimized':<20} {optimized_stats['average']:.5f}  {optimized_stats['min']:.5f}  {optimized_stats['max']:.5f}"
    )


if __name__ == "__main__":
    run_benchmark(n=8, trials=5)
