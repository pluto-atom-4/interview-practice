import random
import time

from leetcode.kth_smallest_pair_distance import smallest_distance_pair
from leetcode.kth_smallest_pair_distance_naive import smallest_distance_pair_naive


def generate_nums(n=1000, max_val=10000):
    """
    Generate a list of random integers of length n.
    """
    return [random.randint(0, max_val) for _ in range(n)]

def benchmark(func, nums, k, trials=3):
    durations = []
    for _ in range(trials):
        start = time.time()
        _ = func(nums, k)
        end = time.time()
        durations.append(end - start)
    return {
        "average": sum(durations) / trials,
        "min": min(durations),
        "max": max(durations)
    }

def run_benchmark():
    nums = generate_nums(n=500, max_val=10000)
    k = len(nums) // 2
    print(f"Benchmarking K-th Smallest Pair Distance with n={len(nums)}, k={k}...\n")

    efficient_stats = benchmark(smallest_distance_pair, nums, k)
    naive_stats = benchmark(smallest_distance_pair_naive, nums, k)

    print("⏱️ Timing Results:")
    print(f"{'Algorithm':<25} {'Avg':<10} {'Min':<10} {'Max':<10}")
    print(f"{'Binary Search + Two Pointers':<25} {efficient_stats['average']:.5f}  {efficient_stats['min']:.5f}  {efficient_stats['max']:.5f}")
    print(f"{'Naive Brute Force':<25} {naive_stats['average']:.5f}  {naive_stats['min']:.5f}  {naive_stats['max']:.5f}")

if __name__ == "__main__":
    run_benchmark()
