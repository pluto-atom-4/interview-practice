import random
import time

from leetcode.longest_consecutive_sequence_generators import (
    longest_consecutive_generators,
)
from leetcode.longest_consecutive_sequence_groupby import longest_consecutive_groupby


def generate_data(n=200000, max_val=500000):
    return [random.randint(0, max_val) for _ in range(n)]


def benchmark(func, data, trials=3):
    durations = []
    for _ in range(trials):
        start = time.time()
        func(data)
        end = time.time()
        durations.append(end - start)

    return {
        "avg": sum(durations) / trials,
        "min": min(durations),
        "max": max(durations),
    }


def run_benchmark():
    data = generate_data()

    print("\nBenchmark: Longest Consecutive Sequence\n")

    gen_stats = benchmark(longest_consecutive_generators, data)
    grp_stats = benchmark(longest_consecutive_groupby, data)

    print(f"{'Implementation':<30} {'Avg':<10} {'Min':<10} {'Max':<10}")
    print(f"{'Generator Pipeline':<30} {gen_stats['avg']:.5f}  {gen_stats['min']:.5f}  {gen_stats['max']:.5f}")
    print(f"{'itertools.groupby':<30} {grp_stats['avg']:.5f}  {grp_stats['min']:.5f}  {grp_stats['max']:.5f}")


if __name__ == '__main__':
    run_benchmark()
