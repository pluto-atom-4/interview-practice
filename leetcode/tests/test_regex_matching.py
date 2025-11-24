import pytest

from leetcode.regex_matching import is_match


@pytest.mark.parametrize("s, p, expected", [
    ("aa", "a", False),
    ("aa", "a*", True),
    ("ab", ".*", True),
    ("aab", "c*a*b", True),
    ("mississippi", "mis*is*p*.", False),
    ("", ".*", True),
    ("", "", True),
    ("abc", "abc", True),
    ("abc", "a.c", True),
    ("abcd", "d*", False),
])
def test_regex_matching_cases(s, p, expected):
    assert is_match(s, p) == expected
