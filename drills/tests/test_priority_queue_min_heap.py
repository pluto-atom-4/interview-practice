"""
Test suite for the PriorityQueue class.

This module uses the unittest framework to validate the functionality of the PriorityQueue class.
"""


from drills.priority_queue_min_heap import PriorityQueue, Task


class TestPriorityQueue:
    """Test cases for the PriorityQueue class."""
    
    def test_enqueue_dequeue(self):
        """Test enqueueing and dequeueing tasks."""
        pq = PriorityQueue()
        task1 = Task("Task 1", 5)
        task2 = Task("Task 2", 1)
        task3 = Task("Task 3", 3)

        pq.enqueue(task1)
        pq.enqueue(task2)
        pq.enqueue(task3)

        assert pq.size() == 3

        assert pq.dequeue() == task2  # Highest priority (lowest number)
        assert pq.dequeue() == task3
        assert pq.dequeue() == task1
        assert pq.is_empty()

    def test_peek(self):
        """Test peeking at the highest-priority task."""
        pq = PriorityQueue()
        task1 = Task("Task 1", 5)
        task2 = Task("Task 2", 1)

        pq.enqueue(task1)
        pq.enqueue(task2)

        assert pq.peek() == task2  # Highest priority (lowest number)
        assert pq.size() == 2  # Size should remain unchanged after peek
    
    def test_dequeue_empty(self):
        """Test dequeueing from an empty priority queue."""
        pq = PriorityQueue()
        assert pq.dequeue() is None  # Should return None when empty