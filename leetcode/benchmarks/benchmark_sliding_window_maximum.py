import random
import time

from leetcode.sliding_window_maximum import sliding_window_maximum
from leetcode.sliding_window_maximum_imperative import sliding_window_maximum_imperative


def generate_data(n=200000, max_val=10**6):
    return [random.randint(-max_val, max_val) for _ in range(n)]


def benchmark(func, nums, k, trials=3):
    durations = []

    for _ in range(trials):
        start = time.time()
        func(nums, k)
        end = time.time()
        durations.append(end - start)

    return {
        "avg": sum(durations) / trials,
        "min": min(durations),
        "max": max(durations),
    }


def run_benchmark():
    nums = generate_data()
    k = 500

    print("\nBenchmark: Sliding Window Maximum\n")

    func_stats = benchmark(sliding_window_maximum, nums, k)
    imp_stats = benchmark(sliding_window_maximum_imperative, nums, k)

    print(f"{'Implementation':<35} {'Avg':<10} {'Min':<10} {'Max':<10}")
    print(
        f"{'Functional (immutable queue)':<35} "
        f"{func_stats['avg']:.5f}  {func_stats['min']:.5f}  {func_stats['max']:.5f}"
    )
    print(
        f"{'Imperative (deque)':<35} "
        f"{imp_stats['avg']:.5f}  {imp_stats['min']:.5f}  {imp_stats['max']:.5f}"
    )


if __name__ == "__main__":
    run_benchmark()
