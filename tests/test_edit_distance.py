import pytest

from algorithms.dynamic_programming.edit_distance import edit_distance


def test_identical_words():
    assert edit_distance("kitten", "kitten") == 0


def test_basic_case():
    assert edit_distance("kitten", "sitting") == 3


def test_insert_only():
    assert edit_distance("abc", "abcdef") == 3


def test_delete_only():
    assert edit_distance("abcdef", "abc") == 3


def test_replace_only():
    assert edit_distance("abc", "xyz") == 3


def test_empty_strings():
    assert edit_distance("", "") == 0
    assert edit_distance("abc", "") == 3
    assert edit_distance("", "abc") == 3
