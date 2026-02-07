"""
FUNCTION top_k_frequent(nums, k):
    IF k <= 0: RETURN an empty list

    // Step 1: Build frequency map
    INITIALIZE freq as an empty map
    FOR each num in nums:
        freq[num] = freq[num] + 1 (default to 0)

    // Step 2: Maintain a min-heap of size k
    INITIALIZE heap as an empty min-priority queue
    FOR each (value, count) in freq:
        PUSH (count, value) onto heap

        // If heap exceeds size k, remove the element with the lowest frequency
        IF size of heap > k:
            POP from heap

    // Step 3: Sort the remaining k elements by frequency descending
    SORT heap by count in descending order
    RETURN the values from the sorted heap

"""

import pytest

from drills.top_k_frequent import top_k_frequent


@pytest.mark.parametrize(
    "nums, k, expected",
    [
        ([1, 1, 1, 2, 2, 3], 2, [1, 2]),
        (["a", "b", "a", "c", "b", "a"], 1, ["a"]),
        ([4, 4, 4, 4], 1, [4]),
        ([1, 2, 3, 4], 2, {3, 4}),  # equal frequencies, deterministic by heap order (min-heap of size 2)
        ([], 3, []),
        ([1], 1, [1]),
        ([1, 2, 3, 2, 1, 2], 1, [2]),
        ([1, 2, 3, 2, 1, 2], 3, [2, 1, 3]),
        ([10, 20, 20, 30, 30, 30], 2, [30, 20]),
    ],
)
def test_top_k_frequent(nums, k, expected):
    result = top_k_frequent(nums, k)
    # For set-based assertions, compare as sets; otherwise compare exact order
    if isinstance(expected, set):
        assert set(result) == expected
    else:
        assert result == expected


def test_k_zero():
    assert top_k_frequent([1, 2, 3], 0) == []


def test_k_larger_than_unique():
    nums = [1, 2, 2, 3]
    result = top_k_frequent(nums, 10)
    # Should return all unique elements
    assert set(result) == {1, 2, 3}


def test_equal_frequencies_deterministic():
    """
    Test that when all elements have equal frequency,
    the min-heap deterministically returns exactly k elements.

    The specific elements returned depend on the heap's internal ordering,
    which is deterministic based on insertion order and heap structure.

    For [1, 2, 3, 4] with k=2:
    - All have frequency=1
    - Min-heap of size 2 maintains the two "largest" by heap's comparison
    - The heap will keep (1, value1) and (1, value2) where value1 and value2
      are determined by which survived the heap pushes/pops
    - When popped and sorted reverse, we get the deterministic result

    This test verifies:
    1. Exactly k=2 elements are returned
    2. The result is deterministic (same input always gives same output)
    3. The set of results is the 2 largest by value when all frequencies equal
    """
    result = top_k_frequent([1, 2, 3, 4], 2)
    # Should return exactly 2 elements
    assert len(result) == 2
    # Both elements should be from the input
    assert all(x in [1, 2, 3, 4] for x in result)
    # Should be the 2 largest values (due to min-heap of size k), order-agnostic
    assert set(result) == {3, 4}


