import pytest

from algorithms.greedy.activity_selection import select_activities


def test_basic_selection():
    activities = [(1, 4), (3, 5), (0, 6), (5, 7), (8, 9), (5, 9)]
    result = select_activities(activities)
    assert result == [(1, 4), (5, 7), (8, 9)]

def test_no_overlap():
    activities = [(1, 2), (3, 4), (5, 6)]
    result = select_activities(activities)
    assert result == activities

def test_all_overlap():
    activities = [(1, 5), (2, 6), (3, 7)]
    result = select_activities(activities)
    assert result == [(1, 5)]

def test_empty_input():
    assert select_activities([]) == []

def test_single_activity():
    assert select_activities([(2, 3)]) == [(2, 3)]
