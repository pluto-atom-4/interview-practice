"""
Custom Sort Function Explained Step-by-Step
------------------------------------------
The custom_sort_object function sorts a list of Person objects using a flexible approach:
- You can specify any sorting key (e.g., age, height, or a tuple of attributes).
- You can choose ascending or descending order with the reverse parameter.

Step-by-step process (Insertion Sort):
1. Iterate through the list from the second element to the end.
2. For each element, compare it to the sorted portion of the list (to its left) using the key function.
3. Shift elements in the sorted portion to the right until the correct position for the current element is found.
4. Insert the current element at its correct position.
5. Repeat until the entire list is sorted.

This approach mimics Python's built-in sorted function, supporting custom keys and reverse order.

Time Complexity: O(n^2)
Space Complexity: O(n) (due to copying the list)
"""

from dataclasses import dataclass


@dataclass
class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height  # in centimeters

    def __repr__(self):
        return f"{self.name} (Age: {self.age}, Height: {self.height}cm)"


# Custom sort function
# Sorts by age, then by height
def custom_sort_object(items, key=None, reverse=False):
    n = len(items)
    result = items[:]
    if key is None:
        raise ValueError(
            "custom_sort_object requires a key function for custom objects like Person."
        )
    key_fn = key
    for i in range(1, n):
        item = result[i]
        item_key = key_fn(item)
        j = i - 1
        if not reverse:
            while j >= 0 and item_key < key_fn(result[j]):
                result[j + 1] = result[j]
                j -= 1
        else:
            while j >= 0 and item_key > key_fn(result[j]):
                result[j + 1] = result[j]
                j -= 1
        result[j + 1] = item
    return result


# Sample data
people = [
    Person("Alice", 30, 165),
    Person("Bob", 25, 175),
    Person("Charlie", 30, 170),
    Person("Diana", 22, 160),
]

if __name__ == "__main__":
    print("Sorted by age, then height:")
    sorted_people = custom_sort_object(people, key=lambda p: (p.age, p.height))
    for person in sorted_people:
        print(person)

    print("\nSorted by age, then height (reverse):")
    sorted_people_reverse = custom_sort_object(
        people, key=lambda p: (p.age, p.height), reverse=True
    )
    for person in sorted_people_reverse:
        print(person)

    print("\nSorted by height:")
    sorted_by_height = custom_sort_object(people, key=lambda p: p.height)
    for person in sorted_by_height:
        print(person)

    print("\nSorted by height (reverse):")
    sorted_by_height_reverse = custom_sort_object(
        people, key=lambda p: p.height, reverse=True
    )
    for person in sorted_by_height_reverse:
        print(person)

    print("\nSorted by age:")
    sorted_by_age = custom_sort_object(people, key=lambda p: p.age)
    for person in sorted_by_age:
        print(person)

    print("\nSorted by age (reverse):")
    sorted_by_age_reverse = custom_sort_object(
        people, key=lambda p: p.age, reverse=True
    )
    for person in sorted_by_age_reverse:
        print(person)

    # Output:
    # Sorted by age, then height:
    # Diana (Age: 22, Height: 160cm)
    # Bob (Age: 25, Height: 175cm)
    # Alice (Age: 30, Height: 165cm)
    # Charlie (Age: 30, Height: 170cm)
    #
    # Sorted by age, then height (reverse):
    # Charlie (Age: 30, Height: 170cm)
    # Alice (Age: 30, Height: 165cm)
    # Bob (Age: 25, Height: 175cm)
    # Diana (Age: 22, Height: 160cm)
    #
    # Sorted by height:
    # Diana (Age: 22, Height: 160cm)
    # Alice (Age: 30, Height: 165cm)
    # Charlie (Age: 30, Height: 170cm)
    # Bob (Age: 25, Height: 175cm)
    #
    # Sorted by height (reverse):
    # Bob (Age: 25, Height: 175cm)
    # Charlie (Age: 30, Height: 170cm)
    # Alice (Age: 30, Height: 165cm)
    # Diana (Age: 22, Height: 160cm)
    #
    # Sorted by age:
    # Diana (Age: 22, Height: 160cm)
    # Bob (Age: 25, Height: 175cm)
    # Alice (Age: 30, Height: 165cm)
    # Charlie (Age: 30, Height: 170cm)
    #
    # Sorted by age (reverse):
    # Charlie (Age: 30, Height: 170cm)
    # Alice (Age: 30, Height: 165cm)
    # Bob (Age: 25, Height: 175cm)
    # Diana (Age: 22, Height: 160cm)
