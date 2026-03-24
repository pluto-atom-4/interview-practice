"""
Merge sort algorithm with visualization steps.
Yields events for each comparison and merge operation.
"""


def merge_sort(arr):
    """
    Merge sort algorithm that yields step-by-step operations.

    Yields:
        dict: Event with keys:
            - 'type': 'compare' or 'merge'
            - 'indices': list of indices involved
            - 'array': current state of array
    """
    arr = arr.copy()
    
    def merge_sort_helper(arr, left, right):
        """Helper function to recursively sort and merge."""
        if left < right:
            mid = (left + right) // 2
            
            # Recursively sort left half
            yield from merge_sort_helper(arr, left, mid)
            
            # Recursively sort right half
            yield from merge_sort_helper(arr, mid + 1, right)
            
            # Merge the sorted halves
            yield from merge(arr, left, mid, right)
    
    def merge(arr, left, mid, right):
        """Merge two sorted subarrays and yield visualization steps."""
        left_arr = arr[left:mid + 1]
        right_arr = arr[mid + 1:right + 1]
        
        i = j = 0
        k = left
        
        while i < len(left_arr) and j < len(right_arr):
            # Yield comparison event
            yield {
                'type': 'compare',
                'indices': [left + i, mid + 1 + j],
                'array': arr.copy()
            }
            
            if left_arr[i] <= right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            
            k += 1
            
            # Yield merge/placement event
            yield {
                'type': 'merge',
                'indices': [left, right],
                'array': arr.copy()
            }
        
        # Place remaining elements from left array
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1
            
            yield {
                'type': 'merge',
                'indices': [left, right],
                'array': arr.copy()
            }
        
        # Place remaining elements from right array
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1
            
            yield {
                'type': 'merge',
                'indices': [left, right],
                'array': arr.copy()
            }
    
    # Run the merge sort
    yield from merge_sort_helper(arr, 0, len(arr) - 1)
    
    # Yield final done event
    yield {
        'type': 'done',
        'indices': [],
        'array': arr.copy()
    }
