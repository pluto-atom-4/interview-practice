"""
CLASS MaxHeapPriorityQueue:
    CONSTRUCTOR:
        INITIALIZE heap as an empty list

    FUNCTION insert(task, priority):
        APPEND (priority, task) to heap
        heapify_up(last_index)

    FUNCTION heapify_up(index):
        WHILE index > 0:
            parent = (index - 1) / 2
            IF heap[index].priority > heap[parent].priority:
                SWAP heap[index] and heap[parent]
                index = parent
            ELSE:
                BREAK

    FUNCTION extract_max():
        IF heap is empty: RETURN None
        
        SWAP heap[0] and heap[last_index]
        max_item = REMOVE last element from heap
        heapify_down(0)
        RETURN max_item

    FUNCTION heapify_down(index):
        WHILE True:
            left = 2 * index + 1
            right = 2 * index + 2
            largest = index

            IF left < heap_size AND heap[left].priority > heap[largest].priority:
                largest = left
            IF right < heap_size AND heap[right].priority > heap[largest].priority:
                largest = right

            IF largest != index:
                SWAP heap[index] and heap[largest]
                index = largest
            ELSE:
                BREAK

    FUNCTION peek():
        RETURN heap[0] IF NOT empty ELSE None

"""

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
