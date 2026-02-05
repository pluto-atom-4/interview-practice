"""
FUNCTION find_longest_unique_substring(s):
    IF s is empty: RETURN ""

    INITIALIZE last_seen as an empty map
    INITIALIZE start = 0
    INITIALIZE max_length = 0
    INITIALIZE longest_substring = ""

    FOR each index i and character char in s:
        // If character was seen within the current window, shrink window from left
        IF char in last_seen AND last_seen[char] >= start:
            start = last_seen[char] + 1

        // Record/update the position of the current character
        last_seen[char] = i

        // If current window is the largest so far, save it
        current_length = i - start + 1
        IF current_length > max_length:
            max_length = current_length
            longest_substring = substring of s from start to i

    RETURN longest_substring

"""

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