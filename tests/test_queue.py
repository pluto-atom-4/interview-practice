import pytest

from data_structures.stack_n_queue.queue import Queue


def test_enqueue_and_dequeue():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)

    assert q.dequeue() == 1
    assert q.dequeue() == 2
    assert q.dequeue() == 3


def test_peek():
    q = Queue()
    q.enqueue("a")
    assert q.peek() == "a"
    q.enqueue("b")
    assert q.peek() == "a"


def test_is_empty():
    q = Queue()
    assert q.is_empty() is True
    q.enqueue(10)
    assert q.is_empty() is False


def test_size():
    q = Queue()
    for i in range(5):
        q.enqueue(i)
    assert q.size() == 5
    assert len(q) == 5


def test_dequeue_empty_raises():
    q = Queue()
    with pytest.raises(IndexError):
        q.dequeue()


def test_peek_empty_raises():
    q = Queue()
    with pytest.raises(IndexError):
        q.peek()
