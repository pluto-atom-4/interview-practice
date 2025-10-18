import pytest

from algorithms.dynamic_programming.lcs import (
    longest_common_subsequence_memo, visualize_lcs_table)


def test_memoized_lcs():
    assert longest_common_subsequence_memo("abcde", "ace") == 3
    assert longest_common_subsequence_memo("abc", "def") == 0
    assert longest_common_subsequence_memo("xyz", "xyz") == 3


def test_visualization_runs():
    # This test ensures the visualization function executes without error
    visualize_lcs_table("abcde", "ace")
