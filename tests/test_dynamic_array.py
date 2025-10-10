import pytest

from data_structures.arrays.dynamic_array import DynamicArray


def test_append_and_get():
    da = DynamicArray()
    da.append(10)
    da.append(20)
    assert da.get(0) == 10
    assert da.get(1) == 20


def test_insert():
    da = DynamicArray()
    da.append(1)
    da.append(3)
    da.insert(1, 2)
    assert str(da) == "[1, 2, 3]"


def test_remove():
    da = DynamicArray()
    da.append(5)
    da.append(6)
    da.append(7)
    da.remove(6)
    assert str(da) == "[5, 7]"


def test_insert_out_of_bounds():
    da = DynamicArray()
    with pytest.raises(IndexError):
        da.insert(5, 100)


def test_remove_not_found():
    da = DynamicArray()
    da.append(1)
    with pytest.raises(ValueError):
        da.remove(99)
