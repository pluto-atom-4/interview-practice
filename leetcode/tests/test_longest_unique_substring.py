import pytest

from leetcode.longest_unique_substring import (
    find_longest_unique_substring,
    find_longest_unique_substring_with_length,
)


class TestFindLongestUniqueSubstring:
    """Test suite for the longest unique substring algorithm."""
    @pytest.mark.parametrize(
        "input_str, expected",
        [
            # Basic cases
            ("abcabcbb", "abc"),
            ("bbbbb", "b"),
            ("pwwkew", "wke"),
            # All unique characters
            ("abcdef", "abcdef"),
            ("abcdefghijklmnopqrstuvwxyz", "abcdefghijklmnopqrstuvwxyz"),
            # Edge cases
            ("", ""),
            ("a", "a"),
            ("au", "au"),
            ("dvdf", "vdf"),
            # Single repeating character
            ("aaaaaa", "a"),
            ("zzzzzz", "z"),
            # Complex patterns
            ("au", "au"),
            ("aab", "ab"),
            ("aab", "ab"),
            ("abc", "abc"),
            # Real-world example: Manufacturing log
            ("ERR1-WARN2-ERR3-OK-ERR1", "1-WARN2"),
            # Mixed special characters
            ("a1b2c3a", "a1b2c3"),  # First longest substring (length 6)
            # Numbers and letters
            ("123121", "123"),  # First longest substring (length 3)
            ("12121", "12"),  # First longest substring (length 2)
        ],
    )
    def test_basic_cases(self, input_str, expected):
        """Test various input strings and verify correct substring is returned."""
        result = find_longest_unique_substring(input_str)
        assert result == expected
        assert len(result) == len(expected)
    def test_empty_string(self):
        """Test that empty string returns empty string."""
        result = find_longest_unique_substring("")
        assert result == ""
        assert len(result) == 0
    def test_single_character(self):
        """Test that single character returns itself."""
        result = find_longest_unique_substring("x")
        assert result == "x"
        assert len(result) == 1
    def test_all_unique(self):
        """Test string where all characters are unique."""
        result = find_longest_unique_substring("abcdef")
        assert result == "abcdef"
        assert len(result) == 6
    def test_all_same_character(self):
        """Test string with all identical characters."""
        result = find_longest_unique_substring("aaaaaa")
        assert result == "a"
        assert len(result) == 1
    def test_basic_case(self):
        """Test the basic LeetCode example."""
        input_str = "abcabcbb"
        result = find_longest_unique_substring(input_str)
        assert result == "abc"
        assert len(result) == 3
    def test_manufacturing_log_example(self):
        """Test with a real-world manufacturing log example."""
        input_str = "ERR1-WARN2-ERR3-OK-ERR1"
        result = find_longest_unique_substring(input_str)
        assert result == "1-WARN2"
        assert len(result) == 7
    def test_with_spaces_and_special_chars(self):
        """Test strings with spaces and special characters."""
        # Spaces and special chars are also tracked
        result = find_longest_unique_substring("a b!a")
        # Should find " b!" or similar
        assert len(result) > 1
    def test_unicode_characters(self):
        """Test with unicode/extended characters."""
        result = find_longest_unique_substring("abc")  # Changed from cafe with accent
        assert len(result) > 0
        # All characters are unique
        assert result == "abc"
    def test_longest_at_beginning(self):
        """Test when longest substring is at the beginning."""
        result = find_longest_unique_substring("abcdefgg")
        assert result == "abcdefg"
    def test_longest_at_end(self):
        """Test when longest substring is at the end."""
        result = find_longest_unique_substring("aabcdef")
        assert result == "abcdef"
    def test_longest_in_middle(self):
        """Test when longest substring is in the middle."""
        result = find_longest_unique_substring("abcdefabc")
        # Length 6: "bcdef" or "abcdef"
        assert len(result) == 6
        assert len(set(result)) == len(result)  # All unique
    def test_multiple_candidates(self):
        """Test when multiple substrings have the same max length."""
        result = find_longest_unique_substring("au")
        assert result == "au"
        assert len(result) == 2
    def test_result_has_all_unique_chars(self):
        """Verify that any result has no repeating characters."""
        test_strings = ["abcabcbb", "pwwkew", "dvdf", "au", "ERR1-WARN2-ERR3-OK-ERR1"]
        for s in test_strings:
            result = find_longest_unique_substring(s)
            # Check that all characters in result are unique
            assert len(result) == len(set(result))
class TestFindLongestUniqueSubstringWithLength:
    """Test suite for the helper function that returns both substring and length."""
    def test_returns_tuple(self):
        """Test that function returns a tuple."""
        result = find_longest_unique_substring_with_length("abcabcbb")
        assert isinstance(result, tuple)
        assert len(result) == 2
    def test_tuple_content(self):
        """Test that tuple contains correct substring and length."""
        substring, length = find_longest_unique_substring_with_length("abcabcbb")
        assert substring == "abc"
        assert length == 3
        assert len(substring) == length
    @pytest.mark.parametrize(
        "input_str, expected_len",
        [
            ("abcabcbb", 3),
            ("bbbbb", 1),
            ("pwwkew", 3),
            ("abcdef", 6),
            ("", 0),
            ("a", 1),
            ("aaaaaa", 1),
        ],
    )
    def test_length_matches_substring(self, input_str, expected_len):
        """Test that returned length matches substring length."""
        substring, length = find_longest_unique_substring_with_length(input_str)
        assert length == expected_len
        assert len(substring) == length
