import pytest

from drills.skip_list import SkipList


def test_insert_and_search():
    sl = SkipList()
    sl.insert("a", 1.0)
    sl.insert("b", 2.0)
    sl.insert("c", 3.0)

    assert sl.search("a") == 1.0
    assert sl.search("b") == 2.0
    assert sl.search("c") == 3.0
    assert sl.search("missing") is None


def test_update_score():
    sl = SkipList()
    sl.insert("user", 10.0)
    assert sl.search("user") == 10.0

    sl.insert("user", 5.0)  # update score
    assert sl.search("user") == 5.0


def test_remove_existing_and_missing():
    sl = SkipList()
    sl.insert("a", 1.0)
    sl.insert("b", 2.0)

    assert sl.remove("a") is True
    assert sl.search("a") is None
    assert len(sl) == 1

    assert sl.remove("not-there") is False


@pytest.mark.parametrize(
    "items, min_s, max_s, expected",
    [
        ([("a", 1.0), ("b", 2.0), ("c", 3.0)], 1.5, 3.5, [("b", 2.0), ("c", 3.0)]),
        ([("x", 5.0), ("y", 10.0), ("z", 15.0)], 0, 6, [("x", 5.0)]),
        ([("a", 1.0), ("b", 1.0), ("c", 1.0)], 1.0, 1.0, [("a", 1.0), ("b", 1.0), ("c", 1.0)]),
    ],
)
def test_range_by_score(items, min_s, max_s, expected):
    sl = SkipList()
    for member, score in items:
        sl.insert(member, score)

    assert list(sl.range_by_score(min_s, max_s)) == expected


def test_iteration_sorted_order():
    sl = SkipList()
    sl.insert("c", 3.0)
    sl.insert("a", 1.0)
    sl.insert("b", 2.0)

    assert list(sl) == [("a", 1.0), ("b", 2.0), ("c", 3.0)]
