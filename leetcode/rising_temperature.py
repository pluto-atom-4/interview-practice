"""
Rising Temperature Algorithm Explained Step-by-Step
----------------------------------------------------
The Rising Temperature problem is a practical data processing challenge that identifies days with higher
temperatures compared to their immediate previous day. This problem is commonly used in SQL databases but
can be solved elegantly using functional Python techniques. It demonstrates core programming concepts:
sorting, pairing, filtering, and functional programming patterns that are essential for data manipulation
and interview discussions about algorithm design and code clarity.

Here is how the process works:

1. **Input Format**: Each weather record is a dictionary containing:
   - "id": unique identifier for the weather record
   - "recordDate": date string in "YYYY-MM-DD" format
   - "temperature": integer temperature value
   - Goal: Return list of IDs where temperature > previous day's temperature

2. **Sorting by Date**: Convert string dates to comparable datetime objects and sort.
   - Parse each "YYYY-MM-DD" string using datetime.strptime()
   - Sort records chronologically by date in ascending order
   - Ensures records are in correct temporal sequence for comparison
   - Returns new sorted list (functional approach - no mutation)

3. **Pairing Adjacent Elements**: Create (today, yesterday) tuples for comparison.
   - Use zip() with offset lists: zip(sorted_rows[1:], sorted_rows[:-1])
   - sorted_rows[1:] gives all records from index 1 onwards (today)
   - sorted_rows[:-1] gives all records up to second-to-last (yesterday)
   - zip() pairs each "today" with its corresponding "yesterday"
   - Automatically handles indices and creates clean tuple pairs

4. **Filtering Rising Days**: Select only records where temperature increased.
   - For each (today, yesterday) pair, compare temperatures
   - Filter keeps only pairs where today["temperature"] > yesterday["temperature"]
   - Discards all other records (same temp or decreasing temp)
   - Returns filtered pairs matching the rising temperature criteria

5. **Extracting Result IDs**: Extract and return only the ID from filtered records.
   - Map over filtered pairs to extract today's ID (first element of pair)
   - Convert map object to list for final return value
   - Result is list of IDs in chronological order of rising temperature days
   - Maintains simplicity by returning only what's asked (IDs, not full records)

6. **Functional Programming Benefits**: Pure functions with no side effects.
   - Each step creates new data structures rather than modifying originals
   - Pipeline of operations: sort → zip → filter → map
   - Immutability makes code predictable and easier to reason about
   - Composable functions can be tested and reused independently

Example: weather = [
    {"id": 1, "recordDate": "2015-01-01", "temperature": 10},
    {"id": 2, "recordDate": "2015-01-02", "temperature": 25},
    {"id": 3, "recordDate": "2015-01-03", "temperature": 20},
    {"id": 4, "recordDate": "2015-01-04", "temperature": 30}
]
- After sorting: same order (already sorted by date)
- Pairs: (record2, record1), (record3, record2), (record4, record3)
- Rising temps: (25>10)✓, (20>25)✗, (30>20)✓
- Result: [2, 4] (IDs where temperature increased from previous day)

Time Complexity: O(n log n) where n = number of weather records
- Dominated by sorting step (O(n log n))
- Zip, filter, map all O(n) operations
- Overall: O(n log n)

Space Complexity: O(n) for sorted list and result
- Sorted list creation: O(n)
- Pairs from zip: O(n)
- Filtered results: O(k) where k ≤ n

This algorithm demonstrates data pipeline construction, functional programming patterns, and practical
problem-solving with built-in Python functions. These concepts are valuable for discussing code clarity,
functional paradigms, and efficient data processing in interviews.
"""

from datetime import datetime
from typing import Dict, List


def rising_temperature(weather: List[Dict]) -> List[int]:
    """
    Pure functional solution to Rising Temperature.
    Each row is a dict: {"id": int, "recordDate": "YYYY-MM-DD", "temperature": int}
    """

    # Sort by date (functional: returns new list)
    sorted_rows = sorted(
        weather,
        key=lambda row: datetime.strptime(row["recordDate"], "%Y-%m-%d")
    )

    # Pair each row with its previous row
    paired = zip(sorted_rows[1:], sorted_rows[:-1])

    # Filter rows where today's temp > yesterday's
    rising = filter(
        lambda pair: pair[0]["temperature"] > pair[1]["temperature"],
        paired
    )

    # Extract today's id
    return list(map(lambda pair: pair[0]["id"], rising))
