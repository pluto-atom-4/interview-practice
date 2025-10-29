import pytest

from data_structures.heaps.max_heap import MaxHeap


def test_insert_and_peek():
    heap = MaxHeap()
    heap.insert(5)
    heap.insert(10)
    heap.insert(3)
    assert heap.peek() == 10


def test_extract_max_order():
    heap = MaxHeap()
    for value in [4, 15, 7, 20, 9]:
        heap.insert(value)
    extracted = [heap.extract_max() for _ in range(5)]
    assert extracted == sorted([4, 15, 7, 20, 9], reverse=True)


def test_extract_max_empty():
    heap = MaxHeap()
    with pytest.raises(IndexError):
        heap.extract_max()


def test_peek_empty():
    heap = MaxHeap()
    with pytest.raises(IndexError):
        heap.peek()
