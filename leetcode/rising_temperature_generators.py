"""
Rising Temperature with Generators - Optimized Pipeline Version
----------------------------------------------------------------
This is an advanced implementation of the Rising Temperature problem using Python generators for
memory efficiency and lazy evaluation. While the standard solution creates intermediate lists (sorted,
pairs, filtered), this version streams data through a generator pipeline. Generators are powerful for
handling large datasets, demonstrating advanced Python concepts like lazy evaluation, memory efficiency,
and functional composition. This implementation is excellent for discussing performance optimization,
memory management, and advanced Python patterns in technical interviews.

Here is how the process works:

1. **Initial Sorting Step**: Same as standard version - sort by date.
   - Parse "YYYY-MM-DD" strings to datetime objects for comparison
   - Sort entire weather list chronologically
   - Note: This step still creates a full sorted list (cannot be lazy)
   - Necessary because we need to read ahead to pair consecutive elements

2. **Generator Pipeline**: Stream data through lazy evaluation stages.
   - Generators don't compute values until requested (yield keyword)
   - Memory footprint is constant regardless of input size
   - Process only one element at a time through the pipeline
   - Chain multiple generators together for data transformation

3. **Pairing Generator**: Create (today, yesterday) tuples lazily.
   - zip(sorted_rows[1:], sorted_rows[:-1]) creates the pairing logic
   - Generator expression: (tuple for ... in ...)
   - Yields one pair at a time only when requested
   - Avoids creating full list of all pairs in memory
   - Offset slicing [1:] and [:-1] still creates lists, but only used for zipping

4. **Filtering Generator**: Stream only rising temperature records.
   - Generator expression filters pairs on-demand
   - Condition: today["temperature"] > yesterday["temperature"]
   - Only yields records matching the filter criterion
   - Previous generator is consumed lazily (one pair at a time)
   - Memory never holds entire filtered list

5. **Final Collection**: Materialize results from generator pipeline.
   - List comprehension [row["id"] for row in rising]
   - Consumes the entire rising generator pipeline
   - Extracts IDs from each yielded record
   - Only at this final step are all results collected into a list
   - Memory consumed only for the final result (not intermediate stages)

6. **Generator Benefits vs Standard Approach**:
   - Standard: sort → full list of pairs → full filtered list → final result
   - Generators: sort → stream pairs → stream filtered → final result
   - Memory savings proportional to number of non-rising days
   - Demonstrates lazy evaluation and functional composition
   - Good for large datasets where most records might be filtered out

Example with same weather data:
- Sorting: [record1, record2, record3, record4] (full list created)
- Pairing generator: yields (record2, record1), then (record3, record2), then (record4, record3)
- Filtering generator: yields record2 (25>10), skips record3, yields record4 (30>20)
- Final list comprehension: collects [2, 4]
- Memory at each step: 1 pair + 1 ID in memory at a time during pipeline

Time Complexity: O(n log n) where n = number of weather records
- Same as standard version: dominated by sorting
- Generator stages all operate in O(1) per element
- Overall: O(n log n)

Space Complexity: O(1) for generator pipeline (not counting sorted list and final result)
- Sorted list: O(n) - cannot be avoided (must see all data chronologically)
- Active generator pipeline: O(1) - processes one element at a time
- Final result: O(k) where k ≤ n (number of rising temperature days)
- Overall: O(n) for sorted + result, but streaming pipeline uses O(1) internal memory

Comparison with Standard Implementation:
- Standard creates intermediate list of all pairs: uses O(n) memory
- Generator approach streams pairs: uses O(1) pipeline memory
- When k << n (few rising days), generators are much more efficient
- When k ≈ n (most days rising), memory savings are minimal but benefits code clarity

This implementation is valuable for interviews discussing:
- Generator functions and lazy evaluation patterns
- Memory efficiency and optimization techniques
- Functional programming pipelines in Python
- Performance considerations for large-scale data processing
- Trade-offs between code clarity and resource optimization
"""

from datetime import datetime
from typing import Dict, List


def rising_temperature_generators(weather: List[Dict]) -> List[int]:
    """
    Pure functional generator‑pipeline version of Rising Temperature.
    """

    # Step 1: sort by date (returns a new list, still functional)
    sorted_rows = sorted(
        weather,
        key=lambda row: datetime.strptime(row["recordDate"], "%Y-%m-%d")
    )

    # Step 2: create a generator of (today, yesterday) pairs
    paired = (
        (today, yesterday)
        for today, yesterday in zip(sorted_rows[1:], sorted_rows[:-1])
    )

    # Step 3: filter only rising temperature days
    rising = (
        today
        for today, yesterday in paired
        if today["temperature"] > yesterday["temperature"]
    )

    # Step 4: extract IDs
    return [row["id"] for row in rising]
