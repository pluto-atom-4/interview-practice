from leetcode.benchmarks.benchmark_median_two_sorted_arrays import (
    benchmark,
    generate_arrays,
)
from leetcode.median_two_sorted_arrays import find_median_sorted_arrays
from leetcode.median_two_sorted_arrays_naive import find_median_sorted_arrays_naive


def test_benchmark_runs():
    nums1, nums2 = generate_arrays(size1=100, size2=100)
    optimal_stats = benchmark(find_median_sorted_arrays, nums1, nums2, trials=1)
    naive_stats = benchmark(find_median_sorted_arrays_naive, nums1, nums2, trials=1)
    assert optimal_stats["average"] >= 0
    assert naive_stats["average"] >= 0
