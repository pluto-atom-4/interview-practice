import pytest

from drills.find_longest_unique_substring import find_longest_unique_substring


class TestLongestUniqueSubstring:
    """Test suite for find_longest_unique_substring function."""

    @pytest.mark.parametrize("input_str,expected", [
        ("abcabcbb", "abc"),
        ("bbbbb", "b"),
        ("pwwkew", "wke"),
        ("", ""),
        ("au", "au"),
        ("dvdf", "vdf"),
    ])
    def test_longest_unique_substring(self, input_str, expected):
        """Test longest unique substring with various cases."""
        result = find_longest_unique_substring(input_str)
        assert result == expected, f"Expected '{expected}', got '{result}'"