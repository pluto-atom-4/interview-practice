import pytest

from data_structures.hash_table.hash_map import HashMap


def test_put_and_get():
    hm = HashMap()
    hm.put("apple", 10)
    hm.put("banana", 20)
    assert hm.get("apple") == 10
    assert hm.get("banana") == 20

def test_update_value():
    hm = HashMap()
    hm.put("key", 1)
    hm.put("key", 99)
    assert hm.get("key") == 99

def test_remove_key():
    hm = HashMap()
    hm.put("x", 42)
    hm.remove("x")
    with pytest.raises(KeyError):
        hm.get("x")

def test_contains_key():
    hm = HashMap()
    hm.put("exists", 123)
    assert hm.contains("exists")
    assert not hm.contains("missing")

def test_get_missing_key():
    hm = HashMap()
    with pytest.raises(KeyError):
        hm.get("ghost")
