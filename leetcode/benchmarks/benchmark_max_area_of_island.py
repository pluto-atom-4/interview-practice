import copy
import random
import time

from leetcode.max_area_of_island import max_area_of_island
from leetcode.max_area_of_island_bfs import max_area_of_island_bfs


def generate_grid(rows=200, cols=200, land_prob=0.3):
    """
    Generate a random grid with given dimensions.
    land_prob controls the probability of a cell being land (1).
    """
    return [[1 if random.random() < land_prob else 0 for _ in range(cols)] for _ in range(rows)]

def benchmark(func, grid, trials=3):
    durations = []
    for _ in range(trials):
        grid_copy = copy.deepcopy(grid)  # avoid mutation
        start = time.time()
        _ = func(grid_copy)
        end = time.time()
        durations.append(end - start)
    return {
        "average": sum(durations) / trials,
        "min": min(durations),
        "max": max(durations)
    }

def run_benchmark():
    grid = generate_grid(rows=300, cols=300, land_prob=0.4)
    print(f"Benchmarking Max Area of Island with grid size {len(grid)}x{len(grid[0])}...\n")

    dfs_stats = benchmark(max_area_of_island, grid)
    bfs_stats = benchmark(max_area_of_island_bfs, grid)

    print("⏱️ Timing Results:")
    print(f"{'Algorithm':<20} {'Avg':<10} {'Min':<10} {'Max':<10}")
    print(f"{'DFS':<20} {dfs_stats['average']:.5f}  {dfs_stats['min']:.5f}  {dfs_stats['max']:.5f}")
    print(f"{'BFS':<20} {bfs_stats['average']:.5f}  {bfs_stats['min']:.5f}  {bfs_stats['max']:.5f}")

if __name__ == "__main__":
    run_benchmark()
