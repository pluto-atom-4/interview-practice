import pytest

from leetcode.merge_k_sorted_lists import (
    build_linked_list,
    linked_list_to_list,
    merge_k_lists,
)


def test_example1():
    lists = [
        build_linked_list([1,4,5]),
        build_linked_list([1,3,4]),
        build_linked_list([2,6])
    ]
    result = merge_k_lists(lists)
    assert linked_list_to_list(result) == [1,1,2,3,4,4,5,6]

def test_example2_empty():
    lists = []
    result = merge_k_lists(lists)
    assert linked_list_to_list(result) == []

def test_example3_empty_list():
    lists = [build_linked_list([])]
    result = merge_k_lists(lists)
    assert linked_list_to_list(result) == []

def test_single_list():
    lists = [build_linked_list([1,2,3])]
    result = merge_k_lists(lists)
    assert linked_list_to_list(result) == [1,2,3]

def test_all_empty_lists():
    lists = [build_linked_list([]), build_linked_list([])]
    result = merge_k_lists(lists)
    assert linked_list_to_list(result) == []
