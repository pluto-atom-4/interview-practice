import pytest

from leetcode.range_sum_query_mutable import NumArray


def test_basic_operations():
    arr = NumArray([1, 3, 5])
    assert arr.sumRange(0, 2) == 9

    arr.update(1, 2)
    assert arr.sumRange(0, 2) == 8


def test_single_element():
    arr = NumArray([7])
    assert arr.sumRange(0, 0) == 7

    arr.update(0, 10)
    assert arr.sumRange(0, 0) == 10


def test_multiple_updates():
    arr = NumArray([2, 4, 6, 8, 10])
    assert arr.sumRange(1, 3) == 18

    arr.update(2, 1)
    assert arr.sumRange(1, 3) == 13

    arr.update(4, 0)
    assert arr.sumRange(0, 4) == 15


def test_edge_ranges():
    arr = NumArray([5, -2, 7, 3])
    assert arr.sumRange(0, 3) == 13
    assert arr.sumRange(1, 1) == -2
    assert arr.sumRange(2, 3) == 10
