"""
Benchmark: AVL Tree vs Red-Black Tree

WHAT THIS BENCHMARK GIVES YOU
==============================
This script provides a fair comparison between AVL Trees and Red-Black Trees
across three critical operations: insertion, search, and deletion.

Fair Comparison
  - Both trees receive identical workloads in the same order
  - Same dataset size and distribution
  - Multiple trials per operation for stable, reliable timing

Large Dataset
  - 20,000 node insertions
  - 5,000 searches (random sample from inserted values)
  - 20,000 node deletions

Reliable Results
  - Each operation runs 3 trials
  - Reports average time (plus min/max available)
  - Measured in seconds

SAMPLE OUTPUT
=============
Benchmark: AVL Tree vs Red-Black Tree

Operation       AVL Avg      RBT Avg
---------------------------------------------
Insert          0.19304     0.05910
Search          0.00750     0.00047
Delete          0.32904     0.10164

KEY INSIGHTS
============
- AVL Trees: More frequent rotations due to stricter balance constraints
  → Slower insertions/deletions but potentially faster searches
- Red-Black Trees: Fewer rotations due to relaxed balance constraints
  → Faster insertions/deletions, competitive search performance

Use this benchmark to understand the performance trade-offs and choose
the data structure best suited for your use case.
"""

import random
import time

from data_structures.trees.avl_tree import AVLNode, AVLTree
from data_structures.trees.red_black_tree import RBNode, RedBlackTree

# ------------------------------------------------------------
# Benchmark helpers
# ------------------------------------------------------------

def benchmark(func, *args, trials=3):
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


# ------------------------------------------------------------
# Workloads
# ------------------------------------------------------------

def workload_insert_avl(values):
    tree = AVLTree()
    root = None
    for v in values:
        root = tree.insert(root, v)
    return root


def workload_insert_rbt(values):
    tree = RedBlackTree()
    root = None
    for v in values:
        root = tree.insert(root, v)
    return root


def workload_search_avl(root, values):
    tree = AVLTree()
    for v in values:
        tree.search(root, v)


def workload_search_rbt(root, values):
    tree = RedBlackTree()
    for v in values:
        tree.search(root, v)


def workload_delete_avl(values):
    tree = AVLTree()
    root = None
    for v in values:
        root = tree.insert(root, v)
    for v in values:
        root = tree.delete(root, v)


def workload_delete_rbt(values):
    tree = RedBlackTree()
    root = None
    for v in values:
        root = tree.insert(root, v)
    for v in values:
        root = tree.delete(root, v)


# ------------------------------------------------------------
# Main benchmark
# ------------------------------------------------------------

def run_benchmark():
    print("\nBenchmark: AVL Tree vs Red‑Black Tree\n")

    N = 20_000
    values = list(range(N))
    random.shuffle(values)

    # INSERT
    avl_insert = benchmark(workload_insert_avl, values)
    rbt_insert = benchmark(workload_insert_rbt, values)

    # SEARCH
    avl_root = workload_insert_avl(values)
    rbt_root = workload_insert_rbt(values)

    search_values = random.sample(values, 5000)

    avl_search = benchmark(workload_search_avl, avl_root, search_values)
    rbt_search = benchmark(workload_search_rbt, rbt_root, search_values)

    # DELETE
    avl_delete = benchmark(workload_delete_avl, values)
    rbt_delete = benchmark(workload_delete_rbt, values)

    # PRINT RESULTS
    print(f"{'Operation':<15} {'AVL Avg':<12} {'RBT Avg':<12}")
    print("-" * 45)
    print(f"{'Insert':<15} {avl_insert['avg']:.5f}     {rbt_insert['avg']:.5f}")
    print(f"{'Search':<15} {avl_search['avg']:.5f}     {rbt_search['avg']:.5f}")
    print(f"{'Delete':<15} {avl_delete['avg']:.5f}     {rbt_delete['avg']:.5f}")


if __name__ == "__main__":
    run_benchmark()
