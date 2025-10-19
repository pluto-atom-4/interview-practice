import pytest

from algorithms.dynamic_programming.knapsack import (knapsack, knapsack_memo,
                                                     knapsack_with_items)


def test_basic_case():
    weights = [1, 3, 4, 5]
    values = [1, 4, 5, 7]
    capacity = 7
    expected = 9
    assert knapsack(weights, values, capacity) == expected
    assert knapsack_memo(weights, values, capacity) == expected


def test_exact_fit():
    weights = [2, 2, 4]
    values = [3, 4, 8]
    capacity = 6
    expected = 12  # items 1 and 2: weights 2+4=6, values 4+8=12
    assert knapsack(weights, values, capacity) == expected
    assert knapsack_memo(weights, values, capacity) == expected


def test_zero_capacity():
    weights = [1, 2, 3]
    values = [10, 20, 30]
    capacity = 0
    expected = 0
    assert knapsack(weights, values, capacity) == expected
    assert knapsack_memo(weights, values, capacity) == expected


def test_empty_items():
    assert knapsack([], [], 10) == 0
    assert knapsack_memo([], [], 10) == 0


def test_large_capacity():
    weights = [2, 3, 4, 5]
    values = [3, 4, 5, 6]
    capacity = 10
    expected = 13  # items 0,1,3: weights 2+3+5=10, values 3+4+6=13
    assert knapsack(weights, values, capacity) == expected
    assert knapsack_memo(weights, values, capacity) == expected


def test_knapsack_with_items_basic():
    weights = [1, 3, 4, 5]
    values = [1, 4, 5, 7]
    capacity = 7
    max_value, items = knapsack_with_items(weights, values, capacity)
    assert max_value == 9
    assert items == [1, 2]  # Items with weights 3 and 4


def test_knapsack_with_items_exact_fit():
    weights = [2, 2, 4]
    values = [3, 4, 8]
    capacity = 6
    max_value, items = knapsack_with_items(weights, values, capacity)
    assert max_value == 12  # items 1 and 2: weights 2+4=6, values 4+8=12
    assert set(items) == {1, 2}  # Items with weights 2 and 4


def test_knapsack_with_items_empty():
    max_value, items = knapsack_with_items([], [], 10)
    assert max_value == 0
    assert items == []


def test_knapsack_with_items_zero_capacity():
    weights = [1, 2, 3]
    values = [10, 20, 30]
    capacity = 0
    max_value, items = knapsack_with_items(weights, values, capacity)
    assert max_value == 0
    assert items == []
