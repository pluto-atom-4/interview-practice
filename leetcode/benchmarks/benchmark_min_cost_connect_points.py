import random
import time

from leetcode.min_cost_connect_points import min_cost_connect_points
from leetcode.min_cost_connect_points_kruskal import min_cost_connect_points_kruskal


def generate_points(n=200, max_val=1000):
    return [[random.randint(0, max_val), random.randint(0, max_val)] for _ in range(n)]

def benchmark(func, points, trials=3):
    durations = []
    for _ in range(trials):
        start = time.time()
        _ = func(points)
        end = time.time()
        durations.append(end - start)
    return {
        "average": sum(durations) / trials,
        "min": min(durations),
        "max": max(durations)
    }

def run_benchmark():
    points = generate_points(n=300, max_val=1000)
    print("Benchmarking Min Cost to Connect Points...\n")

    prim_stats = benchmark(min_cost_connect_points, points, trials=3)
    kruskal_stats = benchmark(min_cost_connect_points_kruskal, points, trials=3)

    print("⏱️ Timing Results:")
    print(f"{'Algorithm':<20} {'Avg':<10} {'Min':<10} {'Max':<10}")
    print(f"{'Prim’s':<20} {prim_stats['average']:.5f}  {prim_stats['min']:.5f}  {prim_stats['max']:.5f}")
    print(f"{'Kruskal’s':<20} {kruskal_stats['average']:.5f}  {kruskal_stats['min']:.5f}  {kruskal_stats['max']:.5f}")

if __name__ == "__main__":
    run_benchmark()
