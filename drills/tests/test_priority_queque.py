import pytest

from drills.priority_queue import MaxHeapPriorityQueue


def test_insert_and_peek():
    pq = MaxHeapPriorityQueue[str]()
    pq.insert("task-low", 1)
    pq.insert("task-high", 10)
    pq.insert("task-mid", 5)

    assert pq.peek() == (10, "task-high")


def test_extract_max_order():
    pq = MaxHeapPriorityQueue[str]()
    pq.insert("A", 3)
    pq.insert("B", 1)
    pq.insert("C", 5)
    pq.insert("D", 4)

    assert pq.extract_max() == (5, "C")
    assert pq.extract_max() == (4, "D")
    assert pq.extract_max() == (3, "A")
    assert pq.extract_max() == (1, "B")
    assert pq.extract_max() is None


def test_size_and_empty():
    pq = MaxHeapPriorityQueue[int]()
    assert pq.is_empty()

    pq.insert(100, 7)
    pq.insert(200, 2)

    assert pq.size() == 2
    assert not pq.is_empty()

    pq.extract_max()
    pq.extract_max()

    assert pq.size() == 0
    assert pq.is_empty()


def test_stability_not_required():
    pq = MaxHeapPriorityQueue[str]()
    pq.insert("task1", 5)
    pq.insert("task2", 5)
    pq.insert("task3", 5)

    priorities = [pq.extract_max()[0] for _ in range(3)]
    assert priorities == [5, 5, 5]
