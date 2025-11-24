import random
import string
import time

from leetcode.regex_matching import is_match
from leetcode.regex_matching_recursive import is_match_recursive


def generate_test_cases(n=100, str_len=20, pat_len=20):
    cases = []
    for _ in range(n):
        s = ''.join(random.choices(string.ascii_lowercase, k=str_len))
        p = ''.join(random.choices(string.ascii_lowercase + ".*", k=pat_len))
        cases.append((s, p))
    return cases

def benchmark(func, cases, trials=3):
    durations = []
    for _ in range(trials):
        start = time.time()
        for s, p in cases:
            func(s, p)
        end = time.time()
        durations.append(end - start)
    return {
        "average": sum(durations) / trials,
        "min": min(durations),
        "max": max(durations)
    }

def run_benchmark():
    cases = generate_test_cases(n=50, str_len=15, pat_len=15)
    print("Benchmarking regex matching implementations...\n")

    dp_stats = benchmark(is_match, cases)
    rec_stats = benchmark(is_match_recursive, cases)

    print("⏱️ Timing Results:")
    print(f"{'Algorithm':<20} {'Avg':<10} {'Min':<10} {'Max':<10}")
    print(f"{'DP':<20} {dp_stats['average']:.5f}  {dp_stats['min']:.5f}  {dp_stats['max']:.5f}")
    print(f"{'Recursive+Memo':<20} {rec_stats['average']:.5f}  {rec_stats['min']:.5f}  {rec_stats['max']:.5f}")

if __name__ == "__main__":
    run_benchmark()
