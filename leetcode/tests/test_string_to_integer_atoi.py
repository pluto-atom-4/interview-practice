import pytest

from leetcode.string_to_integer_atoi import myAtoi


@pytest.mark.parametrize("s, expected", [
    ("42", 42),
    ("   -042", -42),
    ("1337c0d3", 1337),
    ("0-1", 0),
    ("words and 987", 0),
    ("+1", 1),
    ("-91283472332", -2147483648),  # clamp to INT_MIN
    ("91283472332", 2147483647),    # clamp to INT_MAX
    ("   +0 123", 0),
    ("", 0),
    ("   ", 0),
])
def test_myAtoi(s, expected):
    assert myAtoi(s) == expected
