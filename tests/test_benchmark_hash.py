from data_structures.hash_table.benchmark_hash import (
    benchmark_hash_functions,
    generate_keys,
)


def test_hash_distribution():
    keys = generate_keys(n=1000)
    results = benchmark_hash_functions(keys, buckets=128)
    assert results["custom"]["time"] > 0
    assert results["builtin"]["time"] > 0
    assert len(results["custom"]["distribution"]) > 0
    assert len(results["builtin"]["distribution"]) > 0
