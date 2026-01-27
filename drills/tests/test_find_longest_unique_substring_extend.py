"""
Test suite for enhanced find_longest_unique_substring function.
Tests the new max_char_set and allowed_chars parameters.
"""
import pytest

from drills.find_longest_unique_substring_extend import find_longest_unique_substring


class TestLongestUniqueSubstring:
    """Test suite for find_longest_unique_substring function."""

    def test_basic_case(self):
        """Test basic case without filters."""
        result = find_longest_unique_substring("abcabcbb")
        assert result.substring == "abc", f"Expected 'abc', got '{result.substring}'"
        assert result.start == 0
        assert result.end == 2
        assert result.length == 3
        print("✓ test_basic_case passed")


    def test_empty_string(self):
        """Test empty string."""
        result = find_longest_unique_substring("")
        assert result.substring == ""
        assert result.length == 0
        print("✓ test_empty_string passed")


    def test_no_repeats(self):
        """Test string with no repeating characters."""
        result = find_longest_unique_substring("abcdef")
        assert result.substring == "abcdef"
        assert result.length == 6
        print("✓ test_no_repeats passed")


    def test_single_character(self):
        """Test string with single character."""
        result = find_longest_unique_substring("a")
        assert result.substring == "a"
        assert result.length == 1
        print("✓ test_single_character passed")


    def test_all_repeats(self):
        """Test string with all same characters."""
        result = find_longest_unique_substring("aaaa")
        assert result.substring == "a"
        assert result.length == 1
        print("✓ test_all_repeats passed")


    def test_allowed_chars_filter(self):
        """Test with allowed_chars parameter."""
        # Only allow 'a' and 'b'
        result = find_longest_unique_substring("abcabcbb", allowed_chars={'a', 'b'})
        assert result.substring == "ab", f"Expected 'ab', got '{result.substring}'"
        assert result.length == 2
        # Verify all chars in result are from allowed set
        assert all(c in {'a', 'b'} for c in result.substring)
        print("✓ test_allowed_chars_filter passed")


    def test_allowed_chars_empty_result(self):
        """Test when allowed_chars filters out all characters."""
        result = find_longest_unique_substring("abc", allowed_chars={'x', 'y', 'z'})
        assert result.substring == ""
        assert result.length == 0
        print("✓ test_allowed_chars_empty_result passed")


    def test_allowed_chars_single(self):
        """Test with single allowed character."""
        result = find_longest_unique_substring("aabbcc", allowed_chars={'b'})
        assert result.substring == "b"
        assert result.length == 1
        assert all(c == 'b' for c in result.substring)
        print("✓ test_allowed_chars_single passed")


    def test_max_char_set_limit(self):
        """Test max_char_set parameter limits unique characters."""
        # Limit to 3 unique characters
        result = find_longest_unique_substring("abcdefg", max_char_set=3)
        assert result.length == 3, f"Expected length 3, got {result.length}"
        assert len(set(result.substring)) <= 3, f"Expected max 3 unique chars, got {len(set(result.substring))}"
        print(f"✓ test_max_char_set_limit passed: {result.substring}")


    def test_max_char_set_one(self):
        """Test max_char_set=1 (only one unique character allowed)."""
        result = find_longest_unique_substring("aabbcc", max_char_set=1)
        assert result.substring == "a"
        assert result.length == 1
        print("✓ test_max_char_set_one passed")


    def test_max_char_set_large(self):
        """Test max_char_set larger than string alphabet."""
        result = find_longest_unique_substring("abcde", max_char_set=256)
        assert result.substring == "abcde"
        assert result.length == 5
        print("✓ test_max_char_set_large passed")


    def test_combined_filters(self):
        """Test combining allowed_chars and max_char_set."""
        # Allow only 'a', 'b', 'c' but limit to 2 unique characters
        result = find_longest_unique_substring(
            "abcabcabc",
            allowed_chars={'a', 'b', 'c'},
            max_char_set=2
        )
        assert result.length == 2, f"Expected length 2, got {result.length}"
        assert len(set(result.substring)) <= 2
        print(f"✓ test_combined_filters passed: {result.substring}")


    def test_max_char_set_invalid(self):
        """Test invalid max_char_set values."""
        try:
            find_longest_unique_substring("abc", max_char_set=0)
            assert False, "Should raise ValueError for max_char_set=0"
        except ValueError as e:
            assert "max_char_set must be positive" in str(e)
            print("✓ test_max_char_set_invalid passed")


    def test_unicode_characters(self):
        """Test with Unicode characters."""
        result = find_longest_unique_substring("αβγαβ", allowed_chars={'α', 'β', 'γ'})
        assert result.substring == "αβγ"
        assert result.length == 3
        print("✓ test_unicode_characters passed")


    def test_numeric_strings(self):
        """Test with numeric string."""
        result = find_longest_unique_substring("1234512345")
        assert result.substring == "12345"
        assert result.length == 5
        print("✓ test_numeric_strings passed")


    def test_space_and_special_chars(self):
        """Test with spaces and special characters."""
        result = find_longest_unique_substring("a b a!b", allowed_chars={'a', 'b', ' ', '!'})
        assert result.length > 0
        # Verify all chars in result are from allowed set
        assert all(c in {'a', 'b', ' ', '!'} for c in result.substring)
        # Verify no repeating characters in result
        assert len(result.substring) == len(set(result.substring))
        print(f"✓ test_space_and_special_chars passed: '{result.substring}'")
