import random
import time

from leetcode.merge_intervals import merge
from leetcode.merge_intervals_naive import merge_naive


def generate_intervals(n=1000, max_val=10000):
    """
    Generate random intervals.
    """
    intervals = []
    for _ in range(n):
        a, b = random.randint(0, max_val), random.randint(0, max_val)
        intervals.append([min(a, b), max(a, b)])
    return intervals

def benchmark(func, intervals, trials=3):
    durations = []
    for _ in range(trials):
        data = [i[:] for i in intervals]  # copy to avoid mutation
        start = time.time()
        _ = func(data)
        end = time.time()
        durations.append(end - start)
    return {
        "average": sum(durations) / trials,
        "min": min(durations),
        "max": max(durations)
    }

def run_benchmark():
    intervals = generate_intervals(n=2000, max_val=10000)
    print(f"Benchmarking Merge Intervals with n={len(intervals)}...\n")

    greedy_stats = benchmark(merge, intervals)
    naive_stats = benchmark(merge_naive, intervals)

    print("⏱️ Timing Results:")
    print(f"{'Algorithm':<20} {'Avg':<10} {'Min':<10} {'Max':<10}")
    print(f"{'Greedy':<20} {greedy_stats['average']:.5f}  {greedy_stats['min']:.5f}  {greedy_stats['max']:.5f}")
    print(f"{'Naive':<20} {naive_stats['average']:.5f}  {naive_stats['min']:.5f}  {naive_stats['max']:.5f}")

if __name__ == "__main__":
    run_benchmark()
