from algorithms.benchmark.benchmark_activity_selection import (
    benchmark,
    generate_activities,
)
from algorithms.dynamic_programming.activity_selection_dp import select_activities_dp
from algorithms.greedy.activity_selection import select_activities


def test_benchmark_runs():
    activities = generate_activities(n=100)
    greedy = benchmark(select_activities, activities, trials=2)
    dp = benchmark(select_activities_dp, activities, trials=2)
    assert greedy["average"] > 0
    assert dp["average"] > 0
