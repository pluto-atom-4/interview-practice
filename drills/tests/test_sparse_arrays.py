"""
FUNCTION matchingStrings(stringList, queries):
    // Step 1: Build frequency map of stringList
    INITIALIZE freq_map as an empty map
    FOR each s in stringList:
        freq_map[s] = freq_map[s] + 1 (default to 0)

    // Step 2: Map queries to their frequencies
    INITIALIZE results as an empty list
    FOR each q in queries:
        APPEND freq_map[q] (default to 0) to results

    RETURN results
"""

import pytest

from drills.sparse_arrays import matchingStrings


@pytest.mark.parametrize(
    "strings, queries, expected",
    [
        # Basic case: simple matches
        (["a", "b", "a"], ["a", "b", "c"], [2, 1, 0]),
        # No matches
        (["x", "y", "z"], ["a", "b", "c"], [0, 0, 0]),
        # All matches
        (["a", "a", "a"], ["a"], [3]),
        # Mixed matches with duplicates in queries
        (["a", "b", "c", "a"], ["a", "b", "a", "d"], [2, 1, 2, 0]),
        # Empty stringList
        ([], ["a", "b"], [0, 0]),
        # Empty queries
        (["a", "b"], [], []),
        # Large input with many duplicates
        (["a"] * 1000 + ["b"] * 500, ["a", "b", "c"], [1000, 500, 0]),
    ]
)
def test_matchingStrings(strings, queries, expected):
    assert matchingStrings(strings, queries) == expected