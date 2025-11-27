import pytest

from leetcode.permutation_sequence_naive import get_permutation_naive


@pytest.mark.parametrize("n, k, expected", [
    (3, 3, "213"),
    (4, 9, "2314"),
    (3, 1, "123"),
])
def test_get_permutation_naive(n, k, expected):
    assert get_permutation_naive(n, k) == expected
