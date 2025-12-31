import pytest

from data_structures.stack_n_queue.stack import Stack


def test_push_and_pop():
    s = Stack()
    s.push(10)
    s.push(20)
    assert s.pop() == 20
    assert s.pop() == 10


def test_peek():
    s = Stack()
    s.push("a")
    assert s.peek() == "a"
    s.push("b")
    assert s.peek() == "b"


def test_is_empty():
    s = Stack()
    assert s.is_empty() is True
    s.push(1)
    assert s.is_empty() is False


def test_size():
    s = Stack()
    for i in range(5):
        s.push(i)
    assert s.size() == 5


def test_pop_empty_raises():
    s = Stack()
    with pytest.raises(IndexError):
        s.pop()


def test_peek_empty_raises():
    s = Stack()
    with pytest.raises(IndexError):
        s.peek()
