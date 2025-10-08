from functools import lru_cache


@lru_cache(maxsize=None)
def fibonacci(n):
    """
    Recursively calculates the nth Fibonacci number.

    Args:
        n (int): The position in the Fibonacci sequence (0-indexed).

    Returns:
        int: The nth Fibonacci number.
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# Example usage
if __name__ == "__main__":
    for i in range(10):
        print(f"Fibonacci({i}) = {fibonacci(i)}")
