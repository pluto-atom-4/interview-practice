import pytest

from data_structures.hash_table.custom_hash import custom_hash


def test_hash_consistency():
    assert custom_hash("hello") == custom_hash("hello")
    assert custom_hash("world") == custom_hash("world")

def test_hash_difference():
    assert custom_hash("hello") != custom_hash("hella")
    assert custom_hash("abc") != custom_hash("abcd")

def test_hash_with_seed():
    h1 = custom_hash("data", seed=123)
    h2 = custom_hash("data", seed=456)
    assert h1 != h2

def test_hash_type_and_range():
    h = custom_hash("test")
    assert isinstance(h, int)
    assert 0 <= h <= 0xFFFFFFFF
