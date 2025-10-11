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
