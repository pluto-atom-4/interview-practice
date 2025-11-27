from leetcode.benchmarks.benchmark_permutation_sequence import benchmark
from leetcode.permutation_sequence import get_permutation
from leetcode.permutation_sequence_naive import get_permutation_naive


def test_benchmark_runs():
    n, k = 5, 10
    factorial_stats = benchmark(get_permutation, n, k, trials=1)
    naive_stats = benchmark(get_permutation_naive, n, k, trials=1)
    assert factorial_stats["average"] >= 0
    assert naive_stats["average"] >= 0
