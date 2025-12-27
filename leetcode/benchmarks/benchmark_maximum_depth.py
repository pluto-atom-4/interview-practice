import random
import time

from leetcode.maximum_depth_array_binary_tree import max_depth_array_tree
from leetcode.maximum_depth_binary_tree import TreeNode, maxDepth

# ------------------------------------------------------------
# Helpers to generate trees in both representations
# ------------------------------------------------------------

def generate_random_array_tree(n, missing_prob=0.2):
    """
    Generate an array-based binary tree with random None holes.
    """
    values = []
    for _ in range(n):
        if random.random() < missing_prob:
            values.append(None)
        else:
            values.append(random.randint(1, 100))
    return values


def array_to_pointer_tree(values):
    """
    Convert array-based tree into pointer-based TreeNode structure.
    """
    if not values or values[0] is None:
        return None

    nodes = [TreeNode(v) if v is not None else None for v in values]

    for i in range(len(values)):
        if nodes[i] is None:
            continue

        left = 2 * i + 1
        right = 2 * i + 2

        if left < len(values):
            nodes[i].left = nodes[left]
        if right < len(values):
            nodes[i].right = nodes[right]

    return nodes[0]


# ------------------------------------------------------------
# Benchmarking utilities
# ------------------------------------------------------------

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


# ------------------------------------------------------------
# Main benchmark
# ------------------------------------------------------------

def run_benchmark():
    print("\n" + "="*70)
    print("Benchmark: Maximum Depth (Array vs Pointer)")
    print("="*70)

    # Display test conditions
    print("\n📋 TEST CONDITIONS:")
    print("-" * 70)
    print("✓ Fair comparison: both trees have identical structure")
    print("✓ Realistic size: 20,000 nodes with random holes (15% sparsity)")
    print("✓ Trials per implementation: 5 runs")
    print("-" * 70)

    # Generate a moderately large tree
    values = generate_random_array_tree(20000, missing_prob=0.15)
    root = array_to_pointer_tree(values)

    print("\n⏱️  Running benchmarks...\n")
    array_stats = benchmark(max_depth_array_tree, values)
    pointer_stats = benchmark(maxDepth, root)

    # Display results table
    print(f"{'Implementation':<30} {'Avg (s)':<12} {'Min (s)':<12} {'Max (s)':<12}")
    print("-" * 70)
    print(
        f"{'Array-based':<30} "
        f"{array_stats['avg']:.6f}  {array_stats['min']:.6f}  {array_stats['max']:.6f}"
    )
    print(
        f"{'Pointer-based':<30} "
        f"{pointer_stats['avg']:.6f}  {pointer_stats['min']:.6f}  {pointer_stats['max']:.6f}"
    )
    print("-" * 70)

    # Calculate performance difference
    speedup = array_stats['avg'] / pointer_stats['avg']
    print(f"\n📊 PERFORMANCE ANALYSIS:")
    print("-" * 70)
    if speedup > 1:
        print(f"✓ Pointer-based is {speedup:.2f}x faster than array-based")
    else:
        print(f"✓ Array-based is {1/speedup:.2f}x faster than pointer-based")

    # Provide interpretation
    print("\n💡 WHY POINTER‑BASED TENDS TO BE FASTER:")
    print("-" * 70)
    print("1. No index arithmetic")
    print("   - Direct memory references via pointers")
    print("   - Array-based requires computing indices: 2*i+1, 2*i+2")
    print()
    print("2. No bounds checks")
    print("   - Pointer-based: just check if left/right is None")
    print("   - Array-based: must check if index < len(array)")
    print()
    print("3. Direct references instead of array lookups")
    print("   - Pointer: one memory dereference to access child")
    print("   - Array: index calculation + array lookup + null check")
    print()
    print("4. CPU cache efficiency")
    print("   - Pointer-based: sequential traversal benefits from locality")
    print("   - Array-based: sparse arrays may have cache misses")
    print("-" * 70 + "\n")


if __name__ == "__main__":
    run_benchmark()
