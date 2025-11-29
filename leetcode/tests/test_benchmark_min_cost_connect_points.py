from leetcode.benchmarks.benchmark_min_cost_connect_points import (
    benchmark,
    generate_points,
)
from leetcode.min_cost_connect_points import min_cost_connect_points
from leetcode.min_cost_connect_points_kruskal import min_cost_connect_points_kruskal


def test_benchmark_runs():
    points = generate_points(n=50, max_val=100)
    prim_stats = benchmark(min_cost_connect_points, points, trials=1)
    kruskal_stats = benchmark(min_cost_connect_points_kruskal, points, trials=1)
    assert prim_stats["average"] >= 0
    assert kruskal_stats["average"] >= 0
