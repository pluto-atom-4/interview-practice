from leetcode.asteroid_collision import asteroid_collision
from leetcode.benchmarks.benchmark_asteroid_collision import (
    benchmark,
    generate_asteroids,
)


def test_benchmark_runs():
    asteroids = generate_asteroids(n=1000, max_size=50)
    stats = benchmark(asteroid_collision, asteroids, trials=1)
    assert stats["average"] >= 0
    assert stats["min"] >= 0
    assert stats["max"] >= 0
