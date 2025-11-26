import random
import time

from leetcode.median_two_sorted_arrays import find_median_sorted_arrays
from leetcode.median_two_sorted_arrays_naive import find_median_sorted_arrays_naive


def generate_arrays(size1=1000, size2=1000, max_val=10000):
    nums1 = sorted(random.randint(0, max_val) for _ in range(size1))
    nums2 = sorted(random.randint(0, max_val) for _ in range(size2))
    return nums1, nums2

def benchmark(func, nums1, nums2, trials=3):
    durations = []
    for _ in range(trials):
        start = time.time()
        _ = func(nums1, nums2)
        end = time.time()
        durations.append(end - start)
    return {
        "average": sum(durations) / trials,
        "min": min(durations),
        "max": max(durations)
    }

def run_benchmark():
    nums1, nums2 = generate_arrays(size1=5000, size2=5000)
    print("Benchmarking Median of Two Sorted Arrays...\n")

    optimal_stats = benchmark(find_median_sorted_arrays, nums1, nums2)
    naive_stats = benchmark(find_median_sorted_arrays_naive, nums1, nums2)

    print("⏱️ Timing Results:")
    print(f"{'Algorithm':<20} {'Avg':<10} {'Min':<10} {'Max':<10}")
    print(f"{'Optimal (Binary Search)':<20} {optimal_stats['average']:.5f}  {optimal_stats['min']:.5f}  {optimal_stats['max']:.5f}")
    print(f"{'Naive (Merge)':<20} {naive_stats['average']:.5f}  {naive_stats['min']:.5f}  {naive_stats['max']:.5f}")

if __name__ == "__main__":
    run_benchmark()
