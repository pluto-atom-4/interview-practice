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
