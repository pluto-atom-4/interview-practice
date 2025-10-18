import pytest

from algorithms.dynamic_programming.lcs import longest_common_subsequence


def test_basic_case():
    assert longest_common_subsequence("abcde", "ace") == 3


def test_no_common_subsequence():
    assert longest_common_subsequence("abc", "def") == 0


def test_identical_strings():
    assert longest_common_subsequence("xyz", "xyz") == 3


def test_empty_string():
    assert longest_common_subsequence("", "abc") == 0
    assert longest_common_subsequence("abc", "") == 0


def test_partial_overlap():
    assert longest_common_subsequence("abc", "ab") == 2
