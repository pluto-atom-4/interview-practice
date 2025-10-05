"""
Utility functions for interview practice.
These helpers can be reused across problems and tests.
"""

import time
from typing import Any, List


def print_array(arr: List[Any]) -> None:
    """
    Nicely prints a list of elements.

    Args:
        arr (List[Any]): List to print.
    """
    print("[" + ", ".join(str(x) for x in arr) + "]")


def time_execution(func):
    """
    Decorator to measure execution time of a function.

    Usage:
        @time_execution
        def my_function():
            ...
    """

    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time: {end - start:.6f} seconds")
        return result

    return wrapper


def is_sorted(arr: List[int]) -> bool:
    """
    Checks if a list is sorted in ascending order.

    Args:
        arr (List[int]): List to check.

    Returns:
        bool: True if sorted, False otherwise.
    """
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))
