import random
import time

from leetcode.permutations_ii import permute_unique
from leetcode.permutations_ii_itertools import permute_unique_itertools


def generate_nums(n=8, max_val=3):
    """
    Generate a list of length n with values in range [1..max_val].
    """
    return [random.randint(1, max_val) for _ in range(n)]

def benchmark(func, nums, trials=3):
    durations = []
    for _ in range(trials):
        start = time.time()
        _ = func(nums)
        end = time.time()
        durations.append(end - start)
    return {
        "average": sum(durations) / trials,
        "min": min(durations),
        "max": max(durations)
    }

def run_benchmark():
    nums = generate_nums(n=9, max_val=3)
    print(f"Benchmarking Permutations II with nums={nums}...\n")

    backtrack_stats = benchmark(permute_unique, nums)
    itertools_stats = benchmark(permute_unique_itertools, nums)

    print("⏱️ Timing Results:")
    print(f"{'Algorithm':<25} {'Avg':<10} {'Min':<10} {'Max':<10}")
    print(f"{'Backtracking':<25} {backtrack_stats['average']:.5f}  {backtrack_stats['min']:.5f}  {backtrack_stats['max']:.5f}")
    print(f"{'Itertools+Dedup':<25} {itertools_stats['average']:.5f}  {itertools_stats['min']:.5f}  {itertools_stats['max']:.5f}")

if __name__ == "__main__":
    run_benchmark()
