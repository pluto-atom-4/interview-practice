import pytest

from algorithms.sorting.merge_sort import merge_sort
from algorithms.sorting.quick_sort import quick_sort
from algorithms.sorting.sort_custom_object import Person, custom_sort_object

# List of sorting functions to test
SORT_FUNCS = [quick_sort, merge_sort]


@pytest.mark.parametrize("sort_func", SORT_FUNCS)
@pytest.mark.parametrize(
    "input_list,expected",
    [
        ([], []),
        ([5], [5]),
        ([1, 2, 3], [1, 2, 3]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ([3, 1, 4, 1, 5, 9, 2], sorted([3, 1, 4, 1, 5, 9, 2])),
        ([5, 3, 5, 3, 5], sorted([5, 3, 5, 3, 5])),
        ([-3, -1, -4, 2, 0], sorted([-3, -1, -4, 2, 0])),
    ]
)
def test_sorting(sort_func, input_list, expected):
    assert sort_func(input_list) == expected


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
    sorted_people = custom_sort_object(input_people, key=lambda p: (p.age, p.height))
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
    sorted_people = custom_sort_object(
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
    sorted_people = custom_sort_object(input_people, key=key)
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
    sorted_people = custom_sort_object(input_people, key=key, reverse=True)
    assert [p.name for p in sorted_people] == expected_names
