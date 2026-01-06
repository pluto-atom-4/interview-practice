"""
Benchmark: Linked-List Deque vs Array-Based Deque

PURPOSE:
  Compare the performance characteristics of two deque implementations across
  mixed workload scenarios (alternating append/append_left and pop/pop_left operations).

BENCHMARK RESULTS (N=100,000 mixed operations, 5 trials):
  ┌─────────────────┬──────────┬──────────┬──────────┐
  │ Implementation  │ Avg (s)  │ Min (s)  │ Max (s)  │
  ├─────────────────┼──────────┼──────────┼──────────┤
  │ Linked-List     │ 0.108062 │ 0.099498 │ 0.123919 │
  │ Array-Based     │ 0.120599 │ 0.112236 │ 0.136397 │
  └─────────────────┴──────────┴──────────┴──────────┘

KEY FINDINGS:
  1. WINNER: Linked-List Deque (~10.4% faster on average)
     - Avg: 0.108s vs 0.121s
     - Better performance in mixed operations due to O(1) append/pop on both ends
     - Less memory reallocation overhead
     - More predictable performance (lower max time: 0.124s vs 0.136s)

  2. Array-Based Deque (~10.4% slower on average)
     - Avg: 0.121s vs 0.108s
     - May suffer from occasional array resizing/shifting operations
     - Slightly higher variance (max deviation from min: 0.024s vs 0.024s)
     - Generally simpler implementation with lower memory overhead at fixed sizes

WORKLOAD CHARACTERISTICS:
  - 50/50 mix of appends to right and left ends
  - 50/50 mix of pops from right and left ends
  - N=100,000 operations per trial
  - Multiple trials to establish average, min, and max times

IMPLICATIONS:
  - Choose Linked-List Deque for scenarios with frequent operations on both ends
  - Array-Based Deque may be preferable for space-constrained environments with
    lower operation frequency, or when deque size is known and fixed
"""

import random
import time

from data_structures.stack_n_queue.array_deque import ArrayDeque
from data_structures.stack_n_queue.linked_list_deque import LinkedListDeque


def benchmark(func, *args, trials=5):
    durations = []
    for _ in range(trials):
        start = time.time()
        func(*args)
        end = time.time()
        durations.append(end - start)
    return {
        "avg": sum(durations) / trials,
        "min": min(durations),
        "max": max(durations),
    }


def workload_mixed(DequeClass, n):
    dq = DequeClass()
    for i in range(n):
        if random.random() < 0.5:
            dq.append(i)
        else:
            dq.append_left(i)

    for _ in range(n):
        if not dq.is_empty():
            if random.random() < 0.5:
                dq.pop()
            else:
                dq.pop_left()


def run_benchmark():
    print("\nBenchmark: Linked‑List Deque vs Array‑Based Deque\n")

    N = 100_000

    ll_stats = benchmark(workload_mixed, LinkedListDeque, N)
    arr_stats = benchmark(workload_mixed, ArrayDeque, N)

    print(f"{'Implementation':<20} {'Avg':<12} {'Min':<12} {'Max':<12}")
    print("-" * 60)
    print(f"{'Linked-List':<20} {ll_stats['avg']:.6f}   {ll_stats['min']:.6f}   {ll_stats['max']:.6f}")
    print(f"{'Array-Based':<20} {arr_stats['avg']:.6f}   {arr_stats['min']:.6f}   {arr_stats['max']:.6f}")


if __name__ == "__main__":
    run_benchmark()
