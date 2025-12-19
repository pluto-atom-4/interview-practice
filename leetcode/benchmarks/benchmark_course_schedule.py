import random
import time

from leetcode.course_schedule_generators import canFinish_generators
from leetcode.course_schedule_imperative import canFinish_imperative
from leetcode.course_schedule_reduce import canFinish_reduce


def generate_data(numCourses=2000, edges=3000):
    return (
        numCourses,
        [
            [random.randint(0, numCourses - 1), random.randint(0, numCourses - 1)]
            for _ in range(edges)
        ]
    )


def benchmark(func, numCourses, prerequisites, trials=3):
    durations = []

    for _ in range(trials):
        start = time.time()
        func(numCourses, prerequisites)
        end = time.time()
        durations.append(end - start)

    return {
        "avg": sum(durations) / trials,
        "min": min(durations),
        "max": max(durations),
    }


def run_benchmark():
    numCourses, prerequisites = generate_data()

    print("\nBenchmark: Course Schedule Implementations\n")

    gen_stats = benchmark(canFinish_generators, numCourses, prerequisites)
    red_stats = benchmark(canFinish_reduce, numCourses, prerequisites)
    imp_stats = benchmark(canFinish_imperative, numCourses, prerequisites)

    print(f"{'Implementation':<30} {'Avg':<10} {'Min':<10} {'Max':<10}")
    print(f"{'Generator Pipeline':<30} {gen_stats['avg']:.5f}  {gen_stats['min']:.5f}  {gen_stats['max']:.5f}")
    print(f"{'Reduce-based':<30} {red_stats['avg']:.5f}  {red_stats['min']:.5f}  {red_stats['max']:.5f}")
    print(f"{'Imperative DFS':<30} {imp_stats['avg']:.5f}  {imp_stats['min']:.5f}  {imp_stats['max']:.5f}")


if __name__ == "__main__":
    run_benchmark()
