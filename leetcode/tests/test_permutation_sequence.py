import pytest

from leetcode.permutation_sequence import get_permutation


@pytest.mark.parametrize("n, k, expected", [
    (3, 3, "213"),   # Example 1
    (4, 9, "2314"),  # Example 2
    (3, 1, "123"),   # Example 3
    (4, 1, "1234"),  # First permutation
    (4, 24, "4321"), # Last permutation
])
def test_get_permutation(n, k, expected):
    assert get_permutation(n, k) == expected

def test_edge_cases():
    assert get_permutation(1, 1) == "1"
    assert get_permutation(2, 2) == "21"
