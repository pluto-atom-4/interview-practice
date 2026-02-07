"""
FUNCTION find_first_non_repeating(s):
    IF s is empty: RETURN None

    INITIALIZE freq as an empty map (dictionary)

    // First pass: Build the frequency map
    FOR each character ch in s:
        freq[ch] = freq[ch] + 1 (default to 0 if not present)

    // Second pass: Find the first char with a count of one
    FOR each character ch in s:
        IF freq[ch] EQUALS 1:
            RETURN ch

    RETURN None
"""

import pytest

from drills.first_non_repeating_char import find_first_non_repeating


@pytest.mark.parametrize(
    "s, expected",
    [
        ("aabbcde", "c"),
        ("aabbccddeeffg", "g"),
        ("xxyz", "y"),
        ("abcdef", "a"),
        ("a", "a"),
        ("", None),
        (None, None),
        ("aabbcc", None),
        ("swiss", "w"),
        ("1122334455667", "7"),
        ("aazbcdeaf", "z"),
    ],
)
def test_find_first_non_repeating(s, expected):
    assert find_first_non_repeating(s) == expected
