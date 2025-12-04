import random
import time

from leetcode.two_sum import two_sum
from leetcode.two_sum_naive import two_sum_naive


def generate_nums(n=10000, max_val=1000):
    """
    Generate a list of random integers of length n.
    """
    return [random.randint(0, max_val) for _ in range(n)]

def benchmark(func, nums, target, trials=3):
    durations = []
    for _ in range(trials):
        start = time.time()
        _ = func(nums, target)
        end = time.time()
        durations.append(end - start)
    return {
        "average": sum(durations) / trials,
        "min": min(durations),
        "max": max(durations)
    }

def run_benchmark():
    nums = generate_nums(n=5000, max_val=10000)
    target = nums[0] + nums[-1]  # guaranteed solution
    print(f"Benchmarking Two Sum with n={len(nums)}, target={target}...\n")

    hashmap_stats = benchmark(two_sum, nums, target)
    naive_stats = benchmark(two_sum_naive, nums, target)

    print("⏱️ Timing Results:")
    print(f"{'Algorithm':<20} {'Avg':<10} {'Min':<10} {'Max':<10}")
    print(f"{'Hash Map':<20} {hashmap_stats['average']:.5f}  {hashmap_stats['min']:.5f}  {hashmap_stats['max']:.5f}")
    print(f"{'Naive Double Loop':<20} {naive_stats['average']:.5f}  {naive_stats['min']:.5f}  {naive_stats['max']:.5f}")

if __name__ == "__main__":
    run_benchmark()
