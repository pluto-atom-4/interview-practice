"""
Test suite for merge_k_sorted_lists_divide.py

This test file validates the divide-and-conquer implementation of the merge k sorted lists algorithm.
It ensures correctness across various edge cases and normal scenarios, comparing results with expected outputs.

Test Coverage:
- Basic merging with multiple lists
- Edge cases (empty lists, single list, all empty lists)
- Large numbers and duplicates
- Correctness verification
"""

import pytest

from leetcode.merge_k_sorted_lists import build_linked_list, linked_list_to_list
from leetcode.merge_k_sorted_lists_divide import merge_k_lists_divide


class TestMergeKSortedListsDivide:
    """Test suite for divide-and-conquer merge k sorted lists implementation."""

    def test_example1_basic_merge(self):
        """Test basic case with three sorted lists containing duplicates."""
        lists = [
            build_linked_list([1, 4, 5]),
            build_linked_list([1, 3, 4]),
            build_linked_list([2, 6])
        ]
        result = merge_k_lists_divide(lists)
        assert linked_list_to_list(result) == [1, 1, 2, 3, 4, 4, 5, 6]

    def test_example2_empty_input(self):
        """Test with empty list of lists."""
        lists = []
        result = merge_k_lists_divide(lists)
        assert linked_list_to_list(result) == []

    def test_example3_single_empty_list(self):
        """Test with a single empty linked list."""
        lists = [build_linked_list([])]
        result = merge_k_lists_divide(lists)
        assert linked_list_to_list(result) == []

    def test_single_list(self):
        """Test with only one list provided."""
        lists = [build_linked_list([1, 2, 3])]
        result = merge_k_lists_divide(lists)
        assert linked_list_to_list(result) == [1, 2, 3]

    def test_all_empty_lists(self):
        """Test with multiple empty linked lists."""
        lists = [build_linked_list([]), build_linked_list([])]
        result = merge_k_lists_divide(lists)
        assert linked_list_to_list(result) == []

    def test_two_lists(self):
        """Test merging two sorted lists."""
        lists = [
            build_linked_list([1, 3, 5]),
            build_linked_list([2, 4, 6])
        ]
        result = merge_k_lists_divide(lists)
        assert linked_list_to_list(result) == [1, 2, 3, 4, 5, 6]

    def test_many_lists(self):
        """Test merging many lists (tests divide-and-conquer depth)."""
        lists = [
            build_linked_list([1, 5]),
            build_linked_list([2, 6]),
            build_linked_list([3, 7]),
            build_linked_list([4, 8]),
            build_linked_list([9, 10])
        ]
        result = merge_k_lists_divide(lists)
        assert linked_list_to_list(result) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def test_single_element_each(self):
        """Test with lists containing single elements."""
        lists = [
            build_linked_list([5]),
            build_linked_list([2]),
            build_linked_list([8]),
            build_linked_list([1])
        ]
        result = merge_k_lists_divide(lists)
        assert linked_list_to_list(result) == [1, 2, 5, 8]

    def test_duplicates(self):
        """Test with many duplicate values across lists."""
        lists = [
            build_linked_list([1, 1, 1]),
            build_linked_list([1, 1, 1]),
            build_linked_list([1, 1, 1])
        ]
        result = merge_k_lists_divide(lists)
        assert linked_list_to_list(result) == [1, 1, 1, 1, 1, 1, 1, 1, 1]

    def test_large_numbers(self):
        """Test with large integer values."""
        lists = [
            build_linked_list([100, 200, 300]),
            build_linked_list([150, 250, 350]),
            build_linked_list([50, 100, 400])
        ]
        result = merge_k_lists_divide(lists)
        assert linked_list_to_list(result) == [50, 100, 100, 150, 200, 250, 300, 350, 400]

    def test_negative_numbers(self):
        """Test with negative integer values."""
        lists = [
            build_linked_list([-5, -1, 3]),
            build_linked_list([-10, 0, 5]),
            build_linked_list([-3, 2, 4])
        ]
        result = merge_k_lists_divide(lists)
        assert linked_list_to_list(result) == [-10, -5, -3, -1, 0, 2, 3, 4, 5]

    def test_mixed_empty_and_nonempty(self):
        """Test with mix of empty and non-empty lists."""
        lists = [
            build_linked_list([]),
            build_linked_list([1, 2, 3]),
            build_linked_list([]),
            build_linked_list([4, 5, 6])
        ]
        result = merge_k_lists_divide(lists)
        assert linked_list_to_list(result) == [1, 2, 3, 4, 5, 6]

    def test_already_sorted(self):
        """Test when lists are already in merged order."""
        lists = [
            build_linked_list([1, 2]),
            build_linked_list([3, 4]),
            build_linked_list([5, 6])
        ]
        result = merge_k_lists_divide(lists)
        assert linked_list_to_list(result) == [1, 2, 3, 4, 5, 6]

    def test_reverse_order(self):
        """Test when lists are in reverse sorted order."""
        lists = [
            build_linked_list([5, 6]),
            build_linked_list([3, 4]),
            build_linked_list([1, 2])
        ]
        result = merge_k_lists_divide(lists)
        assert linked_list_to_list(result) == [1, 2, 3, 4, 5, 6]

    def test_power_of_two_lists(self):
        """Test with power-of-two number of lists (optimal for divide-and-conquer)."""
        lists = [
            build_linked_list([1, 9]),
            build_linked_list([2, 8]),
            build_linked_list([3, 7]),
            build_linked_list([4, 6]),
            build_linked_list([5])
        ]
        result = merge_k_lists_divide(lists)
        # Note: 5 is not power of 2, but testing with mixed sizes
        assert linked_list_to_list(result) == [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def test_unequal_list_sizes(self):
        """Test with lists of significantly different sizes."""
        lists = [
            build_linked_list([1]),
            build_linked_list([2, 3, 4, 5, 6, 7, 8, 9, 10]),
            build_linked_list([11])
        ]
        result = merge_k_lists_divide(lists)
        assert linked_list_to_list(result) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]


# Parametrized tests for comprehensive coverage
class TestMergeKSortedListsDivideParametrized:
    """Parametrized test cases for merge_k_lists_divide."""

    @pytest.mark.parametrize("input_lists,expected", [
        (
            [[1, 4, 5], [1, 3, 4], [2, 6]],
            [1, 1, 2, 3, 4, 4, 5, 6]
        ),
        (
            [[1], [2], [3]],
            [1, 2, 3]
        ),
        (
            [[5], [1], [3], [2], [4]],
            [1, 2, 3, 4, 5]
        ),
        (
            [[], [1, 2], [3, 4]],
            [1, 2, 3, 4]
        ),
    ])
    def test_various_configurations(self, input_lists, expected):
        """Test various list configurations with parametrization."""
        lists = [build_linked_list(arr) for arr in input_lists]
        result = merge_k_lists_divide(lists)
        assert linked_list_to_list(result) == expected


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

