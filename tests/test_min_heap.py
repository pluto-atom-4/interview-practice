import pytest

from data_structures.heaps.min_heap import MinHeap


def test_insert_and_peek():
    heap = MinHeap()
    heap.insert(5)
    heap.insert(3)
    heap.insert(8)
    assert heap.peek() == 3


def test_extract_min():
    heap = MinHeap()
    heap.insert(10)
    heap.insert(4)
    heap.insert(7)
    assert heap.extract_min() == 4
    assert heap.extract_min() == 7
    assert heap.extract_min() == 10


def test_empty_peek_and_extract():
    heap = MinHeap()
    with pytest.raises(IndexError):
        heap.peek()
    with pytest.raises(IndexError):
        heap.extract_min()


def test_heap_ordering():
    heap = MinHeap()
    values = [9, 1, 6, 3, 5]
    for v in values:
        heap.insert(v)
    sorted_values = [heap.extract_min() for _ in range(len(values))]
    assert sorted_values == sorted(values)
