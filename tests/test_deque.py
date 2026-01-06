import pytest

from data_structures.stack_n_queue.array_deque import ArrayDeque
from data_structures.stack_n_queue.linked_list_deque import LinkedListDeque

DEQUES = [ArrayDeque, LinkedListDeque]


@pytest.mark.parametrize("DequeClass", DEQUES)
def test_append_and_pop(DequeClass):
    dq = DequeClass()
    dq.append(1)
    dq.append(2)
    dq.append(3)
    assert dq.pop() == 3
    assert dq.pop() == 2
    assert dq.pop() == 1


@pytest.mark.parametrize("DequeClass", DEQUES)
def test_append_left_and_pop_left(DequeClass):
    dq = DequeClass()
    dq.append_left(1)
    dq.append_left(2)
    dq.append_left(3)
    assert dq.pop_left() == 3
    assert dq.pop_left() == 2
    assert dq.pop_left() == 1


@pytest.mark.parametrize("DequeClass", DEQUES)
def test_mixed_operations(DequeClass):
    dq = DequeClass()
    dq.append(1)
    dq.append_left(2)
    dq.append(3)
    dq.append_left(4)
    assert dq.pop_left() == 4
    assert dq.pop() == 3
    assert dq.pop_left() == 2
    assert dq.pop() == 1


@pytest.mark.parametrize("DequeClass", DEQUES)
def test_empty_pop_raises(DequeClass):
    dq = DequeClass()
    with pytest.raises(IndexError):
        dq.pop()
    with pytest.raises(IndexError):
        dq.pop_left()
