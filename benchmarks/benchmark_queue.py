"""
Benchmark: Linked-List Queue vs Array-Based Queue

RESULTS INTERPRETATION:
======================

This benchmark compares two queue implementations across three operation types:
- Linked-List Queue: Uses node-based structure with O(1) enqueue/dequeue
- Array-Based Queue: Uses circular buffer with dynamic resizing

KEY FINDINGS:
=============

1. ENQUEUE OPERATIONS (Adding Elements)
   Linked-List: 0.06020 sec ⭐ 40% FASTER
   Array-Based: 0.10184 sec
   → Linked-list wins decisively. No array resizing overhead during append operations.

2. DEQUEUE OPERATIONS (Removing Elements)
   Linked-List: 0.09362 sec
   Array-Based: 0.09962 sec (~6% slower)
   → Nearly identical performance. Both are O(1) operations, minimal difference.

3. MIXED OPERATIONS (50% Enqueue, 50% Dequeue)
   Linked-List: 0.03582 sec
   Array-Based: 0.03944 sec (~10% slower)
   → Linked-list slightly ahead, but both are very fast at smaller workload sizes.

CONCLUSIONS:
============
- Linked-List Queue generally outperforms Array-Based Queue, especially for heavy enqueue
- Primary advantage: No array resizing/reallocation overhead
- Array-Based might be competitive with smarter memory pre-allocation strategies
- For this workload (N=100,000), linked-list is the clear winner
"""

import random
import time

from data_structures.stack_n_queue.array_queue import ArrayQueue
from data_structures.stack_n_queue.queue import Queue


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


def workload_enqueue(queue_class, n):
    q = queue_class()
    for i in range(n):
        q.enqueue(i)


def workload_dequeue(queue_class, n):
    q = queue_class()
    for i in range(n):
        q.enqueue(i)
    for _ in range(n):
        q.dequeue()


def workload_mixed(queue_class, n):
    q = queue_class()
    for i in range(n):
        if random.random() < 0.5:
            q.enqueue(i)
        else:
            if not q.is_empty():
                q.dequeue()


def run_benchmark():
    print("\nBenchmark: Linked‑List Queue vs Array‑Based Queue\n")

    N = 100_000

    ll_enqueue = benchmark(workload_enqueue, Queue, N)
    arr_enqueue = benchmark(workload_enqueue, ArrayQueue, N)

    ll_dequeue = benchmark(workload_dequeue, Queue, N)
    arr_dequeue = benchmark(workload_dequeue, ArrayQueue, N)

    ll_mixed = benchmark(workload_mixed, Queue, N)
    arr_mixed = benchmark(workload_mixed, ArrayQueue, N)

    print(f"{'Operation':<15} {'Linked-List':<15} {'Array-Based':<15}")
    print("-" * 50)
    print(f"{'Enqueue':<15} {ll_enqueue['avg']:.5f}       {arr_enqueue['avg']:.5f}")
    print(f"{'Dequeue':<15} {ll_dequeue['avg']:.5f}       {arr_dequeue['avg']:.5f}")
    print(f"{'Mixed':<15} {ll_mixed['avg']:.5f}       {arr_mixed['avg']:.5f}")


if __name__ == "__main__":
    run_benchmark()
