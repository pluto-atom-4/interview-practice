"""
CLASS MinHeapPriorityQueue:
    CONSTRUCTOR:
        INITIALIZE heap as an empty list

    // Helper functions for array-based tree navigation
    FUNCTION parent(index): RETURN (index - 1) // 2
    FUNCTION left_child(index): RETURN (2 * index) + 1
    FUNCTION right_child(index): RETURN (2 * index) + 2

    FUNCTION insert(task, priority):
        APPEND (priority, task) to the end of heap
        heapify_up(length of heap - 1)

    FUNCTION heapify_up(index):
        WHILE index > 0:
            p_idx = parent(index)
            // If current priority is smaller than parent, swap to maintain min-heap property
            IF heap[index].priority < heap[p_idx].priority:
                SWAP heap[index] WITH heap[p_idx]
                index = p_idx
            ELSE:
                BREAK loop

    FUNCTION extract_min():
        IF heap is empty: RETURN None

        // Swap the root (min) with the last element
        SWAP heap[0] WITH heap[last_index]
        min_item = REMOVE last element from heap

        // Restore heap property from the top down
        IF heap is not empty:
            heapify_down(0)

        RETURN min_item

    FUNCTION heapify_down(index):
        size = length of heap
        WHILE True:
            smallest = index
            L = left_child(index)
            R = right_child(index)

            // Find the smallest among parent, left child, and right child
            IF L < size AND heap[L].priority < heap[smallest].priority:
                smallest = L
            IF R < size AND heap[R].priority < heap[smallest].priority:
                smallest = R

            IF smallest is NOT index:
                SWAP heap[index] WITH heap[smallest]
                index = smallest
            ELSE:
                BREAK loop

"""

import pytest

from drills.priority_queue_min_heap import MinHeapPriorityQueue


def test_insert_and_peek():
    pq = MinHeapPriorityQueue()
    pq.insert("task1", 5)
    pq.insert("task2", 3)
    pq.insert("task3", 7)
    assert pq.peek() == (3, "task2")

def test_extract_min():
    pq = MinHeapPriorityQueue()
    pq.insert("task1", 5)
    pq.insert("task2", 3)
    pq.insert("task3", 7)
    assert pq.extract_min() == (3, "task2")
    assert pq.extract_min() == (5, "task1")
    assert pq.extract_min() == (7, "task3")
    assert pq.extract_min() is None

def test_is_empty_and_size():
    pq = MinHeapPriorityQueue()
    assert pq.is_empty()
    assert pq.size() == 0
    pq.insert("task1", 1)
    assert not pq.is_empty()
    assert pq.size() == 1
    pq.extract_min()
    assert pq.is_empty()
    assert pq.size() == 0

def test_duplicate_priorities():
    pq = MinHeapPriorityQueue()
    pq.insert("task1", 2)
    pq.insert("task2", 2)
    pq.insert("task3", 1)
    assert pq.extract_min() == (1, "task3")
    min1 = pq.extract_min()
    min2 = pq.extract_min()
    assert min1[0] == 2 and min2[0] == 2
    assert {min1[1], min2[1]} == {"task1", "task2"}
    assert pq.extract_min() is None

def test_negative_and_zero_priority():
    pq = MinHeapPriorityQueue()
    pq.insert("task1", 0)
    pq.insert("task2", -5)
    pq.insert("task3", 3)
    assert pq.extract_min() == (-5, "task2")
    assert pq.extract_min() == (0, "task1")
    assert pq.extract_min() == (3, "task3")
    assert pq.extract_min() is None

