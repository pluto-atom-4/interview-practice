"""
Benchmark Script for Merge K Sorted Lists Implementations
==========================================================

This script compares the performance of two merge k sorted lists implementations:
1. Heap-based approach (min-heap priority queue)
2. Divide-and-conquer approach (recursive merging)

The benchmark measures execution time across various test cases with different list sizes
and configurations to help understand the performance characteristics of each algorithm.

Test cases vary by:
- Number of lists (k)
- Length of each list (elements per list)
- Total number of nodes in the merge operation

This benchmark helps determine which approach is more efficient for different scenarios
during job interview discussions and practical applications.
"""

import random
import time

from leetcode.merge_k_sorted_lists import (
    build_linked_list,
    linked_list_to_list,
    merge_k_lists,
)
from leetcode.merge_k_sorted_lists_divide import merge_k_lists_divide


def generate_test_lists(k=10, length=50, max_val=1000):
    """
    Generate k sorted linked lists with specified length and max value.

    Args:
        k (int): Number of linked lists to generate
        length (int): Number of elements in each linked list
        max_val (int): Maximum value for random integers

    Returns:
        list: List of k sorted linked lists (as ListNode objects)
    """
    lists = []
    for _ in range(k):
        arr = sorted(random.randint(0, max_val) for _ in range(length))
        lists.append(build_linked_list(arr))
    return lists


def benchmark(func, lists, func_name="", test_case_name="", trials=1):
    """
    Benchmark a function and display progress.

    Args:
        func (callable): Function to benchmark (e.g., merge_k_lists)
        lists (list): Input linked lists to merge
        func_name (str): Name of the algorithm for display
        test_case_name (str): Description of test case
        trials (int): Number of times to run the function

    Returns:
        dict: Dictionary with 'average', 'min', 'max' timing results in seconds
    """
    durations = []
    for trial in range(trials):
        print(f"  {func_name} - {test_case_name}: Trial {trial + 1}/{trials}...", end="\r")
        start = time.time()
        result = func(lists)
        _ = linked_list_to_list(result)  # force traversal
        end = time.time()
        durations.append(end - start)

    return {
        "average": sum(durations) / trials,
        "min": min(durations),
        "max": max(durations)
    }


def run_benchmark():
    """
    Run comprehensive benchmark with multiple test cases of varying sizes.

    This function:
    1. Generates test cases with different numbers of lists and list sizes
    2. Benchmarks both heap-based and divide-and-conquer implementations
    3. Displays timing results and performance comparison
    4. Summarizes results in a table format
    """
    print("=" * 70)
    print("Benchmarking Merge k Sorted Lists - Multiple Test Cases")
    print("=" * 70)
    print()

    # Test cases with varying sizes: (k, length, description)
    # Each tuple represents:
    # - k: number of sorted lists
    # - length: number of elements in each list
    # - description: human-readable description of the test case
    test_cases = [
        (3, 10, "Small (3 lists, 10 nodes each)"),
        (5, 15, "Medium (5 lists, 15 nodes each)"),
        (8, 20, "Large (8 lists, 20 nodes each)"),
    ]

    results = []

    for k, length, description in test_cases:
        print(f"\n📋 Test Case: {description}")
        print(f"   Total nodes: {k * length}")
        print("-" * 70)

        # Generate test data once, then use it for both implementations
        lists = generate_test_lists(k=k, length=length)

        # Benchmark heap-based implementation
        heap_stats = benchmark(merge_k_lists, lists, func_name="Heap-based",
                              test_case_name=description, trials=1)

        # Regenerate lists for second test (since first implementation consumes them)
        lists = generate_test_lists(k=k, length=length)

        # Benchmark divide-and-conquer implementation
        divide_stats = benchmark(merge_k_lists_divide, lists, func_name="Divide & Conquer",
                                test_case_name=description, trials=1)

        results.append({
            "description": description,
            "heap": heap_stats,
            "divide": divide_stats
        })

        # Display timing results for this test case
        print(f"\n   ⏱️ Timing Results for {description}:")
        print(f"   {'Algorithm':<18} {'Avg (ms)':<12} {'Min (ms)':<12} {'Max (ms)':<12}")
        print(f"   {'-'*54}")
        print(f"   {'Heap-based':<18} {heap_stats['average']*1000:>10.2f}  {heap_stats['min']*1000:>10.2f}  {heap_stats['max']*1000:>10.2f}")
        print(f"   {'Divide & Conquer':<18} {divide_stats['average']*1000:>10.2f}  {divide_stats['min']*1000:>10.2f}  {divide_stats['max']*1000:>10.2f}")

        # Calculate performance difference
        if heap_stats['average'] > 0:
            avg_diff = ((divide_stats['average'] - heap_stats['average']) / heap_stats['average'] * 100)
            faster = "Heap-based" if avg_diff > 0 else "Divide & Conquer"
            print(f"   → {faster} is {abs(avg_diff):.1f}% faster")
        else:
            print(f"   → Both algorithms are extremely fast (< 1ms)")

    # Summary table
    print("\n" + "=" * 70)
    print("📊 SUMMARY")
    print("=" * 70)
    print(f"{'Test Case':<30} {'Heap-based (ms)':<20} {'Divide & Conquer (ms)':<20}")
    print("-" * 70)
    for result in results:
        heap_avg = result['heap']['average'] * 1000
        divide_avg = result['divide']['average'] * 1000
        print(f"{result['description']:<30} {heap_avg:>18.2f}  {divide_avg:>18.2f}")

    print("\n" + "=" * 70)
    print("Key Insights:")
    print("-" * 70)
    print("• Time Complexity:")
    print("  - Heap-based: O(N log k) where N = total nodes, k = number of lists")
    print("  - Divide & Conquer: O(N log k) with different constant factors")
    print()
    print("• Space Complexity:")
    print("  - Heap-based: O(k) for the heap size")
    print("  - Divide & Conquer: O(log k) for recursion depth")
    print()
    print("• Performance Factors:")
    print("  - Heap constant factor overhead")
    print("  - Recursion call overhead")
    print("  - Cache locality in divide-and-conquer")
    print("=" * 70)
    print("\n✅ Benchmark complete!")


if __name__ == "__main__":
    run_benchmark()

