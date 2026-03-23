"""
Bubble sort algorithm with visualization steps.
Yields events for each comparison and swap operation.
"""


def bubble_sort(arr):
    """
    Bubble sort algorithm that yields step-by-step operations.

    Yields:
        dict: Event with keys:
            - 'type': 'compare' or 'swap'
            - 'indices': list of indices involved
            - 'array': current state of array
    """
    arr = arr.copy()
    n = len(arr)

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            # Yield comparison
            yield {
                'type': 'compare',
                'indices': [j, j + 1],
                'array': arr.copy()
            }

            if arr[j] > arr[j + 1]:
                # Swap
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

                yield {
                    'type': 'swap',
                    'indices': [j, j + 1],
                    'array': arr.copy()
                }

        if not swapped:
            break

    yield {
        'type': 'done',
        'indices': [],
        'array': arr.copy()
    }

