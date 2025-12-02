import random
import time

from leetcode.k_closest_points import k_closest
from leetcode.k_closest_points_sort import k_closest_sort


def generate_points(n=10000, max_val=1000):
    return [[random.randint(-max_val, max_val), random.randint(-max_val, max_val)] for _ in range(n)]

def benchmark(func, points, k, trials=3):
    durations = []
    for _ in range(trials):
        start = time.time()
        _ = func(points[:], k)  # copy to avoid in-place modifications
        end = time.time()
        durations.append(end - start)
    return {
        "average": sum(durations) / trials,
        "min": min(durations),
        "max": max(durations)
    }

def run_benchmark():
    points = generate_points(n=20000, max_val=1000)
    k = 5000
    print(f"Benchmarking K Closest Points with n={len(points)}, k={k}...\n")

    heap_stats = benchmark(k_closest, points, k)
    sort_stats = benchmark(k_closest_sort, points, k)

    print("⏱️ Timing Results:")
    print(f"{'Algorithm':<20} {'Avg':<10} {'Min':<10} {'Max':<10}")
    print(f"{'Heap-based':<20} {heap_stats['average']:.5f}  {heap_stats['min']:.5f}  {heap_stats['max']:.5f}")
    print(f"{'Sorting-based':<20} {sort_stats['average']:.5f}  {sort_stats['min']:.5f}  {sort_stats['max']:.5f}")

if __name__ == "__main__":
    run_benchmark()
