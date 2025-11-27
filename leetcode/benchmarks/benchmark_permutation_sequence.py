import time

from leetcode.permutation_sequence import get_permutation
from leetcode.permutation_sequence_naive import get_permutation_naive


def benchmark(func, n, k, trials=3):
    durations = []
    for _ in range(trials):
        start = time.time()
        _ = func(n, k)
        end = time.time()
        durations.append(end - start)
    return {
        "average": sum(durations) / trials,
        "min": min(durations),
        "max": max(durations)
    }

def run_benchmark():
    n, k = 8, 15000  # moderate size for comparison
    print(f"Benchmarking Permutation Sequence with n={n}, k={k}...\n")

    factorial_stats = benchmark(get_permutation, n, k)
    naive_stats = benchmark(get_permutation_naive, n, k)

    print("⏱️ Timing Results:")
    print(f"{'Algorithm':<20} {'Avg':<10} {'Min':<10} {'Max':<10}")
    print(f"{'Factorial Method':<20} {factorial_stats['average']:.5f}  {factorial_stats['min']:.5f}  {factorial_stats['max']:.5f}")
    print(f"{'Naive itertools':<20} {naive_stats['average']:.5f}  {naive_stats['min']:.5f}  {naive_stats['max']:.5f}")

if __name__ == "__main__":
    run_benchmark()
