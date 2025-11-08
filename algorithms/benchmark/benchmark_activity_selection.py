"""
Benchmarking script for Activity Selection Problem algorithms:
---
Compares Greedy and Dynamic Programming approaches.
"""
import random
import time

from algorithms.dynamic_programming.activity_selection_dp import select_activities_dp
from algorithms.greedy.activity_selection import select_activities


def generate_activities(n=1000, max_time=10000):
    activities = []
    for _ in range(n):
        start = random.randint(0, max_time - 10)
        end = start + random.randint(1, 10)
        activities.append((start, end))
    return activities

def benchmark(func, activities, trials=5):
    durations = []
    for _ in range(trials):
        start = time.time()
        func(activities)
        end = time.time()
        durations.append(end - start)
    return {
        "average": sum(durations) / trials,
        "min": min(durations),
        "max": max(durations)
    }

def run_benchmark(n=1000, trials=5):
    activities = generate_activities(n)
    print(f"Benchmarking with {n} activities over {trials} trials...\n")

    greedy_stats = benchmark(select_activities, activities, trials)
    dp_stats = benchmark(select_activities_dp, activities, trials)

    print("⏱️ Timing Results:")
    print(f"{'Algorithm':<20} {'Avg':<10} {'Min':<10} {'Max':<10}")
    print(f"{'Greedy':<20} {greedy_stats['average']:.5f}  {greedy_stats['min']:.5f}  {greedy_stats['max']:.5f}")
    print(f"{'Dynamic Programming':<20} {dp_stats['average']:.5f}  {dp_stats['min']:.5f}  {dp_stats['max']:.5f}")

if __name__ == "__main__":
    run_benchmark()
