import random
import time

from leetcode.asteroid_collision import asteroid_collision


def generate_asteroids(n=100000, max_size=1000):
    """
    Generate a random asteroid array of length n.
    Each asteroid has a random size and random direction.
    """
    return [random.choice([-1, 1]) * random.randint(1, max_size) for _ in range(n)]

def benchmark(func, asteroids, trials=3):
    durations = []
    for _ in range(trials):
        start = time.time()
        _ = func(asteroids)
        end = time.time()
        durations.append(end - start)
    return {
        "average": sum(durations) / trials,
        "min": min(durations),
        "max": max(durations)
    }

def run_benchmark():
    asteroids = generate_asteroids(n=200000, max_size=1000)
    print("Benchmarking asteroid collision algorithm...\n")

    stats = benchmark(asteroid_collision, asteroids, trials=3)

    print("⏱️ Timing Results:")
    print(f"{'Algorithm':<20} {'Avg':<10} {'Min':<10} {'Max':<10}")
    print(f"{'Stack-based':<20} {stats['average']:.5f}  {stats['min']:.5f}  {stats['max']:.5f}")

if __name__ == "__main__":
    run_benchmark()
