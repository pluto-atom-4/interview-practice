"""
Benchmarking custom hash function against Python's built-in hash function.
Measures time taken and distribution spread over a set of generated keys.
"""

import random
import string
import time
from collections import defaultdict

from data_structures.hash_table.custom_hash import custom_hash


def generate_keys(n=10000, length=8):
    return [
        ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        for _ in range(n)
    ]

def benchmark_hash_functions(keys, buckets=1024):
    custom_times = []
    builtin_times = []
    custom_dist = defaultdict(int)
    builtin_dist = defaultdict(int)

    start = time.time()
    for key in keys:
        h = custom_hash(key)
        custom_dist[h % buckets] += 1
    custom_times.append(time.time() - start)

    start = time.time()
    for key in keys:
        h = hash(key)
        builtin_dist[h % buckets] += 1
    builtin_times.append(time.time() - start)

    return {
        "custom": {
            "time": sum(custom_times),
            "distribution": custom_dist
        },
        "builtin": {
            "time": sum(builtin_times),
            "distribution": builtin_dist
        }
    }

def run_benchmark():
    keys = generate_keys()
    results = benchmark_hash_functions(keys)

    print("⏱️ Timing:")
    print(f"Custom Hash:  {results['custom']['time']:.5f} seconds")
    print(f"Built-in Hash: {results['builtin']['time']:.5f} seconds")

    print("\n📊 Distribution Spread (bucket count = 1024):")
    print(f"Custom Hash:  {len(results['custom']['distribution'])} buckets used")
    print(f"Built-in Hash: {len(results['builtin']['distribution'])} buckets used")

if __name__ == "__main__":
    run_benchmark()
