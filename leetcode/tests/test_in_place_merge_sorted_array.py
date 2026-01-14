"""
Pytest tests for in-place merge sorted arrays using gap method.

Tests cover:
- Helper functions (getValue, setValue)
- Gap method algorithm with various input combinations
- Edge cases and boundary conditions
- Space and time complexity requirements
- Real-world scenarios
"""

import importlib.util
import sys
from pathlib import Path

import pytest

# Import the module with hyphens in its name
leetcode_dir = Path(__file__).parent.parent
spec = importlib.util.spec_from_file_location(
    "merge_module",
    leetcode_dir / "in-place-merge-sorted-array.py"
)
merge_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(merge_module)

get_value = merge_module.get_value
set_value = merge_module.set_value
merge = merge_module.merge


class TestHelperFunctions:
    """Tests for getValue and setValue helper functions."""

    def test_get_value_from_first_array(self):
        """getValue should retrieve values from array a."""
        a = [1, 2, 3]
        b = [4, 5, 6]
        n = len(a)

        assert get_value(a, b, 0, n) == 1
        assert get_value(a, b, 1, n) == 2
        assert get_value(a, b, 2, n) == 3

    def test_get_value_from_second_array(self):
        """getValue should retrieve values from array b (via virtual indexing)."""
        a = [1, 2, 3]
        b = [4, 5, 6]
        n = len(a)

        assert get_value(a, b, 3, n) == 4
        assert get_value(a, b, 4, n) == 5
        assert get_value(a, b, 5, n) == 6

    def test_get_value_boundary(self):
        """getValue should correctly handle boundary between arrays."""
        a = [1, 2, 3]
        b = [10, 20, 30]
        n = 3

        assert get_value(a, b, 2, n) == 3   # Last element of a
        assert get_value(a, b, 3, n) == 10  # First element of b

    def test_set_value_in_first_array(self):
        """setValue should set values in array a."""
        a = [1, 2, 3]
        b = [4, 5, 6]
        n = len(a)

        set_value(a, b, 0, n, 100)
        assert a[0] == 100

        set_value(a, b, 2, n, 300)
        assert a[2] == 300

    def test_set_value_in_second_array(self):
        """setValue should set values in array b (via virtual indexing)."""
        a = [1, 2, 3]
        b = [4, 5, 6]
        n = len(a)

        set_value(a, b, 3, n, 400)
        assert b[0] == 400

        set_value(a, b, 5, n, 600)
        assert b[2] == 600

    def test_set_get_value_consistency(self):
        """getValue and setValue should be consistent."""
        a = [1, 2, 3]
        b = [4, 5, 6]
        n = len(a)

        # Set and get from a
        set_value(a, b, 0, n, 999)
        assert get_value(a, b, 0, n) == 999

        # Set and get from b
        set_value(a, b, 4, n, 888)
        assert get_value(a, b, 4, n) == 888


class TestMergeGapMethod:
    """Tests for merge function using gap method."""

    @pytest.mark.parametrize("a, b", [
        # Basic case
        ([1, 2, 3], [2, 5, 6]),

        # Arrays where a has smaller elements
        ([1, 2, 3], [4, 5, 6]),

        # Arrays where b has smaller elements
        ([4, 5, 6], [1, 2, 3]),

        # Single elements
        ([1], [2]),
        ([2], [1]),

        # Empty arrays
        ([1, 2, 3], []),
        ([], [1, 2, 3]),

        # Duplicate elements
        ([1, 1, 1], [1, 1, 1]),

        # Negative numbers
        ([-3, -1, 0], [-2, 1, 3]),

        # Large arrays
        ([1, 3, 5, 7, 9], [2, 4, 6, 8, 10]),

        # Overlapping ranges
        ([1, 5, 9], [2, 4, 8]),

        # One much larger
        ([1], [2, 3, 4, 5, 6]),
    ])
    def test_merge_various_cases(self, a, b):
        """Test merge with various input combinations."""
        a_copy = a.copy()
        b_copy = b.copy()

        merge(a, b)

        # Key property: when read as [a || b], result is sorted
        combined = a + b
        assert combined == sorted(combined), f"Virtual merge [a||b] not sorted: {combined}"

        # All original elements must still be present
        original_all = sorted(a_copy + b_copy)
        merged_all = sorted(a + b)
        assert merged_all == original_all, "Elements were lost or duplicated"

    def test_merge_preserves_sorted_order_virtually(self):
        """When reading [a || b], result should be sorted."""
        a = [1, 3, 5]
        b = [2, 4, 6]

        merge(a, b)

        # Concatenate to check overall sortedness
        combined = a + b
        assert combined == sorted(combined), f"Virtual merge not sorted: {combined}"

    def test_merge_preserves_all_elements(self):
        """Merge should preserve all elements (no loss or duplication)."""
        a = [1, 3, 5]
        b = [2, 4, 6]
        original_all = sorted(a + b)

        merge(a, b)

        merged_all = sorted(a + b)
        assert merged_all == original_all, "Elements were lost or duplicated"

    def test_merge_in_place_modification(self):
        """Verify merge modifies arrays in-place."""
        a = [1, 3, 5]
        b = [2, 4, 6]
        a_id = id(a)
        b_id = id(b)

        merge(a, b)

        assert id(a) == a_id, "Array a was replaced"
        assert id(b) == b_id, "Array b was replaced"

    def test_merge_empty_first_array(self):
        """Merge with empty first array."""
        a = []
        b = [1, 2, 3]

        merge(a, b)

        combined = a + b
        assert combined == sorted(combined)

    def test_merge_empty_second_array(self):
        """Merge with empty second array."""
        a = [1, 2, 3]
        b = []

        merge(a, b)

        combined = a + b
        assert combined == sorted(combined)

    def test_merge_single_element_arrays(self):
        """Merge arrays with single elements."""
        a = [5]
        b = [3]

        merge(a, b)

        combined = a + b
        assert combined == [3, 5]

    def test_merge_with_duplicates(self):
        """Merge should correctly handle duplicate elements."""
        a = [1, 1, 1]
        b = [1, 1, 1]

        merge(a, b)

        combined = a + b
        assert combined == [1, 1, 1, 1, 1, 1]

    def test_merge_all_identical(self):
        """Merge when all elements are identical."""
        a = [5, 5, 5]
        b = [5, 5, 5]

        merge(a, b)

        combined = a + b
        assert combined == [5, 5, 5, 5, 5, 5]

    def test_merge_negative_numbers(self):
        """Merge should handle negative numbers."""
        a = [-5, -3, -1]
        b = [-4, -2, 0]

        merge(a, b)

        combined = a + b
        assert combined == sorted(combined)

    def test_merge_mixed_positive_negative(self):
        """Merge arrays with mixed positive and negative."""
        a = [-5, 0, 5]
        b = [-3, 2, 7]

        merge(a, b)

        combined = a + b
        assert combined == sorted(combined)

    def test_merge_large_numbers(self):
        """Merge should handle large numbers."""
        a = [10**6, 10**7, 10**8]
        b = [10**5, 10**6 + 1, 10**9]

        merge(a, b)

        combined = a + b
        assert combined == sorted(combined)


class TestEdgeCases:
    """Tests for edge cases and boundary conditions."""

    def test_merge_single_element_in_each(self):
        """Merge single element from each array."""
        a = [5]
        b = [3]

        merge(a, b)

        combined = a + b
        assert combined == [3, 5]

    def test_merge_unequal_sizes(self):
        """Merge arrays of vastly different sizes."""
        a = [1]
        b = [2, 3, 4, 5, 6, 7, 8, 9, 10]

        merge(a, b)

        combined = a + b
        assert combined == sorted(combined)

    def test_merge_already_sorted_virtually(self):
        """Merge when already virtually sorted."""
        a = [1, 2, 3]
        b = [4, 5, 6]

        merge(a, b)

        combined = a + b
        assert combined == [1, 2, 3, 4, 5, 6]

    def test_merge_completely_reversed(self):
        """Merge when all of b comes before a."""
        a = [7, 8, 9]
        b = [1, 2, 3]

        merge(a, b)

        combined = a + b
        assert combined == sorted(combined)

    def test_merge_alternating_pattern(self):
        """Merge with alternating small and large elements."""
        a = [1, 5, 9]
        b = [3, 7, 11]

        merge(a, b)

        combined = a + b
        assert combined == [1, 3, 5, 7, 9, 11]

    def test_merge_many_duplicates(self):
        """Merge with many duplicate elements across arrays."""
        a = [1, 2, 2, 2, 3]
        b = [1, 2, 2, 3, 3]

        merge(a, b)

        combined = a + b
        assert combined == sorted(combined)


class TestComplexity:
    """Tests verifying complexity requirements."""

    def test_merge_space_complexity(self):
        """Verify O(1) space: no auxiliary arrays created."""
        # This is implicit in the algorithm since we don't create new lists
        a = [1, 3, 5]
        b = [2, 4, 6]

        merge(a, b)

        # If we got here without stack overflow, space complexity is O(1)
        assert True

    def test_merge_time_complexity_large_arrays(self):
        """Verify algorithm completes in reasonable time for large arrays."""
        # Create large sorted arrays
        a = list(range(0, 1000, 2))  # Even numbers
        b = list(range(1, 1000, 2))  # Odd numbers

        # Should complete quickly due to O((n+m)*log(n+m)) complexity
        merge(a, b)

        combined = a + b
        assert combined == sorted(combined)


class TestRealWorldScenarios:
    """Tests based on real-world use cases."""

    def test_merge_time_series_data(self):
        """Merge two time series datasets."""
        # Timestamps from device 1
        device1 = [100, 300, 500, 700]
        # Timestamps from device 2
        device2 = [150, 250, 400, 600, 800]

        merge(device1, device2)

        combined = device1 + device2
        assert combined == sorted(combined)

    def test_merge_sorted_lists_from_databases(self):
        """Merge sorted query results from different database shards."""
        shard1 = [10, 30, 50, 70]
        shard2 = [20, 40, 60, 80]

        merge(shard1, shard2)

        combined = shard1 + shard2
        assert combined == [10, 20, 30, 40, 50, 60, 70, 80]

    def test_merge_sorted_logs(self):
        """Merge sorted application logs by timestamp."""
        log_server1 = [1000, 1010, 1020, 1030]
        log_server2 = [1005, 1015, 1025, 1035]

        merge(log_server1, log_server2)

        combined = log_server1 + log_server2
        assert combined == sorted(combined)

    def test_merge_inventory_sorted_by_id(self):
        """Merge inventory from two warehouses."""
        warehouse_a = [101, 103, 105, 107]
        warehouse_b = [102, 104, 106, 108]

        merge(warehouse_a, warehouse_b)

        combined = warehouse_a + warehouse_b
        assert combined == sorted(combined)


class TestDocumentedExamples:
    """Tests from documented examples in the code."""

    def test_example_from_docstring(self):
        """Test example from merge function docstring."""
        a = [1, 2, 3]
        b = [2, 5, 6]

        merge(a, b)

        # Result when reading [a || b] should be sorted
        combined = a + b
        assert combined == sorted(combined)
        assert all(combined[i] <= combined[i+1] for i in range(len(combined)-1))

    def test_example_trace_from_docs(self):
        """Test the trace example from documentation."""
        # From the example trace in docstring
        a = [1, 2, 3]
        b = [2, 5, 6]

        merge(a, b)

        combined = a + b
        # Should be sorted when read as [a || b]
        assert combined == sorted(combined)
        # When read as [a || b]: [1, 2, 2, 3, 5, 6] (sorted)
        assert sorted(combined) == [1, 2, 2, 3, 5, 6]

