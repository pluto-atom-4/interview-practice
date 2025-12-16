import pytest

from leetcode.string_to_integer_atoi_reduce import myAtoi_reduce


@pytest.mark.parametrize("s, expected", [
    ("42", 42),
    ("   -042", -42),
    ("1337c0d3", 1337),
    ("0-1", 0),
    ("words and 987", 0),
    ("-91283472332", -2147483648),
    ("91283472332", 2147483647),
])
def test_myAtoi_reduce(s, expected):
    assert myAtoi_reduce(s) == expected
