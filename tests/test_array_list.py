import pytest

from data_structures.lists.array_list import ArrayList


def test_append_and_prepend():
    arr = ArrayList()
    arr.append(2)
    arr.append(3)
    arr.prepend(1)
    assert arr.to_array() == [1, 2, 3]


def test_insert_middle():
    arr = ArrayList()
    arr.append(1)
    arr.append(3)
    arr.insert(1, 2)
    assert arr.to_array() == [1, 2, 3]


def test_delete():
    arr = ArrayList()
    for i in range(5):
        arr.append(i)
    arr.delete(2)
    assert arr.to_array() == [0, 1, 3, 4]


def test_concatenate():
    arr = ArrayList()
    arr.append(1)
    arr.append(2)
    arr.concatenate([3, 4])
    assert arr.to_array() == [1, 2, 3, 4]


def test_sort():
    arr = ArrayList()
    arr.append(3)
    arr.append(1)
    arr.append(2)
    arr.sort()
    assert arr.to_array() == [1, 2, 3]


def test_set_size():
    arr = ArrayList()
    arr.append(1)
    arr.append(2)
    arr.set_size(5)
    assert len(arr) == 5
    assert arr.to_array() == [1, 2, None, None, None]

    arr.set_size(1)
    assert arr.to_array() == [1]


def test_extend_capacity():
    arr = ArrayList(capacity=2)
    arr.extend_capacity(10)
    assert arr._capacity == 10


def test_get_set_item():
    arr = ArrayList()
    arr.append(10)
    arr.append(20)
    arr[1] = 99
    assert arr[1] == 99

def test_shrink_after_delete():
    arr = ArrayList(capacity=8)

    # Fill to capacity
    for i in range(8):
        arr.append(i)

    assert arr._capacity == 8

    # Remove elements until size <= capacity/4
    arr.delete(0)  # size = 7
    arr.delete(0)  # size = 6
    arr.delete(0)  # size = 5
    arr.delete(0)  # size = 4  (4 <= 8/4 → should shrink)

    assert arr._capacity == 4
    assert arr.to_array() == [4, 5, 6, 7]


def test_shrink_does_not_go_below_minimum():
    arr = ArrayList(capacity=4)

    for i in range(4):
        arr.append(i)

    assert arr._capacity == 4

    # Delete until empty
    for _ in range(4):
        arr.delete(0)

    # Should NOT shrink below 4
    assert arr._capacity == 4


def test_shrink_after_set_size():
    arr = ArrayList(capacity=16)

    for i in range(10):
        arr.append(i)

    assert arr._capacity == 16

    # Force size down to 3 → 3 <= 16/4 → shrink
    arr.set_size(3)

    assert arr._capacity == 8  # shrinks to half
    assert len(arr) == 3


def test_no_shrink_too_early():
    arr = ArrayList(capacity=16)

    for i in range(5):
        arr.append(i)

    # size = 5, capacity = 16 → 5 > 16/4 → no shrink
    arr.delete(0)  # size = 4
    # still 4 > 16/4 → no shrink yet

    assert arr._capacity == 16


def test_shrink_multiple_times():
    arr = ArrayList(capacity=32)

    for i in range(20):
        arr.append(i)

    assert arr._capacity == 32

    # Remove until size <= 32/4 = 8 → shrink to 16
    for _ in range(12):
        arr.delete(0)

    assert arr._capacity == 16

    # Remove until size <= 16/4 = 4 → shrink to 8
    for _ in range(4):
        arr.delete(0)

    assert arr._capacity == 8
