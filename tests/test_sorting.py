import pytest

from algorithms.sorting.merge_sort import merge_sort
from algorithms.sorting.sort_custom_object import Person, custom_sort_people


@pytest.mark.parametrize(
    "input_arr,expected",
    [
        ([5, 2, 4, 6, 1, 3], [1, 2, 3, 4, 5, 6]),
        ([1], [1]),
        ([], []),
        ([9, 7, 5, 3], [3, 5, 7, 9]),
    ],
)
def test_merge_sort(input_arr, expected):
    assert merge_sort(input_arr) == expected


@pytest.mark.parametrize(
    "input_people,expected_names",
    [
        (
            [
                Person("Alice", 30, 165),
                Person("Bob", 25, 175),
                Person("Charlie", 30, 170),
                Person("Diana", 22, 160),
            ],
            ["Diana", "Bob", "Alice", "Charlie"],
        ),
        ([Person("Eve", 40, 180)], ["Eve"]),
        ([], []),
        (
            [
                Person("A", 20, 150),
                Person("B", 20, 150),
                Person("C", 20, 140),
            ],
            ["C", "A", "B"],
        ),
    ],
)
def test_custom_sort_people(input_people, expected_names):
    sorted_people = custom_sort_people(input_people, key=lambda p: (p.age, p.height))
    assert [p.name for p in sorted_people] == expected_names


@pytest.mark.parametrize(
    "input_people,expected_names",
    [
        (
            [
                Person("Alice", 30, 165),
                Person("Bob", 25, 175),
                Person("Charlie", 30, 170),
                Person("Diana", 22, 160),
            ],
            ["Charlie", "Alice", "Bob", "Diana"],
        ),
        ([Person("Eve", 40, 180)], ["Eve"]),
        ([], []),
        (
            [
                Person("A", 20, 150),
                Person("B", 20, 150),
                Person("C", 20, 140),
            ],
            ["A", "B", "C"],
        ),
    ],
)
def test_custom_sort_people_reverse(input_people, expected_names):
    sorted_people = custom_sort_people(
        input_people, key=lambda p: (p.age, p.height), reverse=True
    )
    assert [p.name for p in sorted_people] == expected_names


@pytest.mark.parametrize(
    "input_people,key,expected_names",
    [
        # key: height
        (
            [
                Person("Alice", 30, 165),
                Person("Bob", 25, 175),
                Person("Charlie", 30, 170),
                Person("Diana", 22, 160),
            ],
            lambda p: p.height,
            ["Diana", "Alice", "Charlie", "Bob"],
        ),
        ([Person("Eve", 40, 180)], lambda p: p.height, ["Eve"]),
        ([], lambda p: p.height, []),
        (
            [
                Person("A", 20, 150),
                Person("B", 20, 150),
                Person("C", 20, 140),
            ],
            lambda p: p.height,
            ["C", "A", "B"],
        ),
        # key: age
        (
            [
                Person("Alice", 30, 165),
                Person("Bob", 25, 175),
                Person("Charlie", 30, 170),
                Person("Diana", 22, 160),
            ],
            lambda p: p.age,
            ["Diana", "Bob", "Alice", "Charlie"],
        ),
        ([Person("Eve", 40, 180)], lambda p: p.age, ["Eve"]),
        ([], lambda p: p.age, []),
        (
            [
                Person("A", 20, 150),
                Person("B", 20, 150),
                Person("C", 20, 140),
            ],
            lambda p: p.age,
            ["A", "B", "C"],
        ),
        # key: (age, height)
        (
            [
                Person("Alice", 30, 165),
                Person("Bob", 25, 175),
                Person("Charlie", 30, 170),
                Person("Diana", 22, 160),
            ],
            lambda p: (p.age, p.height),
            ["Diana", "Bob", "Alice", "Charlie"],
        ),
        ([Person("Eve", 40, 180)], lambda p: (p.age, p.height), ["Eve"]),
        ([], lambda p: (p.age, p.height), []),
        (
            [
                Person("A", 20, 150),
                Person("B", 20, 150),
                Person("C", 20, 140),
            ],
            lambda p: (p.age, p.height),
            ["C", "A", "B"],
        ),
    ],
)
def test_custom_sort_people_key(input_people, key, expected_names):
    sorted_people = custom_sort_people(input_people, key=key)
    assert [p.name for p in sorted_people] == expected_names


@pytest.mark.parametrize(
    "input_people,key,expected_names",
    [
        # key: height, reverse
        (
            [
                Person("Alice", 30, 165),
                Person("Bob", 25, 175),
                Person("Charlie", 30, 170),
                Person("Diana", 22, 160),
            ],
            lambda p: p.height,
            ["Bob", "Charlie", "Alice", "Diana"],
        ),
        ([Person("Eve", 40, 180)], lambda p: p.height, ["Eve"]),
        ([], lambda p: p.height, []),
        (
            [
                Person("A", 20, 150),
                Person("B", 20, 150),
                Person("C", 20, 140),
            ],
            lambda p: p.height,
            ["A", "B", "C"],
        ),
        # key: age, reverse
        (
            [
                Person("Alice", 30, 165),
                Person("Bob", 25, 175),
                Person("Charlie", 30, 170),
                Person("Diana", 22, 160),
            ],
            lambda p: p.age,
            ["Alice", "Charlie", "Bob", "Diana"],
        ),
        ([Person("Eve", 40, 180)], lambda p: p.age, ["Eve"]),
        ([], lambda p: p.age, []),
        (
            [
                Person("A", 20, 150),
                Person("B", 20, 150),
                Person("C", 20, 140),
            ],
            lambda p: p.age,
            ["A", "B", "C"],
        ),
        # key: (age, height), reverse
        (
            [
                Person("Alice", 30, 165),
                Person("Bob", 25, 175),
                Person("Charlie", 30, 170),
                Person("Diana", 22, 160),
            ],
            lambda p: (p.age, p.height),
            ["Charlie", "Alice", "Bob", "Diana"],
        ),
        ([Person("Eve", 40, 180)], lambda p: (p.age, p.height), ["Eve"]),
        ([], lambda p: (p.age, p.height), []),
        (
            [
                Person("A", 20, 150),
                Person("B", 20, 150),
                Person("C", 20, 140),
            ],
            lambda p: (p.age, p.height),
            ["A", "B", "C"],
        ),
    ],
)
def test_custom_sort_people_key_reverse(input_people, key, expected_names):
    sorted_people = custom_sort_people(input_people, key=key, reverse=True)
    assert [p.name for p in sorted_people] == expected_names
