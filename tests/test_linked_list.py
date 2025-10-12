import pytest

from data_structures.linked_lists.linked_list import LinkedList


def test_append():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    assert ll.to_list() == [1, 2, 3]


def test_prepend():
    ll = LinkedList()
    ll.append(2)
    ll.prepend(1)
    assert ll.to_list() == [1, 2]


def test_delete():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.delete(2)
    assert ll.to_list() == [1, 3]


def test_find():
    ll = LinkedList()
    ll.append(10)
    ll.append(20)
    assert ll.find(10) is True
    assert ll.find(99) is False


def test_reverse():
    ll = LinkedList()
    for val in [1, 2, 3, 4]:
        ll.append(val)
    ll.reverse()
    assert ll.to_list() == [4, 3, 2, 1]


def test_insert_at_index():
    ll = LinkedList()
    ll.append(1)
    ll.append(3)
    ll.insert_at_index(1, 2)  # Insert 2 between 1 and 3
    assert ll.to_list() == [1, 2, 3]

    ll.insert_at_index(0, 0)  # Insert 0 at the beginning
    assert ll.to_list() == [0, 1, 2, 3]

    ll.insert_at_index(4, 4)  # Insert 4 at the end
    assert ll.to_list() == [0, 1, 2, 3, 4]

    with pytest.raises(IndexError):
        ll.insert_at_index(10, 99)  # Invalid index
