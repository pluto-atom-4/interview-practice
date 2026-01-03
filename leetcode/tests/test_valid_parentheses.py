import pytest

from leetcode.valid_parentheses import is_valid_parentheses


@pytest.mark.parametrize(
    "input_str,expected",
    [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("{[]}", True),
        ("", True),
        ("(((((())))))", True),
        ("(((()", False),
        ("abc", False),  # invalid characters
    ]
)
def test_valid_parentheses(input_str, expected):
    assert is_valid_parentheses(input_str) == expected
