"""
## Problem Statement

Count how many times each query string appears in a given string list. 
Return the counts in the same order as the queries, matching the position and duplicates exactly.
This tests understanding of hash tables for frequency counting and the importance of preserving order.

## Whiteboard Coding Challenge Notes

* For this problem, I'm using a **Two-Pass Hash Table approach**:

  The solution builds a frequency map in one pass, then retrieves counts in a second pass. 
  This decouples building the frequency data from answering queries, making it simple and efficient.

* Key Concepts:

  - **Why a Hash Table (Dictionary)?**
    Hash tables provide O(1) average-case lookup for frequency counts. 
    Instead of searching through the entire list for each query (which would be O(n*m)), 
    we precompute all frequencies once. Trade-off: O(n) space to store frequencies vs. O(n*m) time without it.

  - **Why two passes instead of one?**
    Separating frequency building from query answering makes the code clearer and reusable. 
    If we had multiple query sets, we'd only build the map once. For a single query set, 
    two passes is simple and readable without performance loss (both O(n) + O(m) = O(n+m) overall).

  - **Why use `freq_map.get(q, 0)` instead of checking if key exists?**
    The `.get()` method with a default value handles missing keys elegantly in one operation. 
    If a query never appears in the list, this returns 0 without exceptions, avoiding explicit conditionals.

* Logic:

1. **Initialize** an empty dictionary to store frequency counts
2. **First Pass:** Iterate through stringList, counting each unique string
3. **Second Pass:** For each query, retrieve its count from the dictionary (default to 0 if not found)
4. **Return** the list of counts in query order

* **30-Second Pitch**:

I'm using a hash table to count string frequencies. First, I build a dictionary with one pass through 
the string list. Then for each query, I look up its count in the dictionary—returning 0 if it's not there. 
This gives us O(n+m) time and O(n) space, avoiding the O(n*m) cost of searching for each query.

* **Rapid-Fire Version**:

- Build a frequency map from stringList in O(n) time
- Look up each query's count in O(1) using dictionary `.get()`
- Return counts in query order, defaulting to 0 for missing strings
- Time: O(n+m) | Space: O(n) for the frequency map

* **Ultra-Minimal One-Liner**:

Use a hash table to count string frequencies in one pass, then answer each query with O(1) lookups.

* **Complexity Analysis**:

- **Time Complexity:** O(n + m), where n = length of stringList and m = number of queries. 
  We iterate through stringList once to build the map (O(n)), then iterate through queries once to look up counts (O(m)).
- **Space Complexity:** O(n) in the worst case, storing one entry per unique string in stringList.

* **Use Cases**:

This pattern is useful for any problem requiring fast repeated lookups after preprocessing: 
counting word frequencies for text analysis, deduplicating API requests, or handling repeated queries efficiently.
"""

from typing import Dict, List


def matchingStrings(stringList:List[str], queries:List[str]) -> List[int]:
    """
    two path sequence loop using Hash Table using the query as a key
    INIT hash
    LOOP (1): build the hash table
    LOOP (2): each of string list

    Counts occurrences of each query in stringList using a Hash Table.
    Ensures the output order matches the queries list exactly.
    """
    # Step 1: Build frequency map of stringList
    # This is O(n) time complexity
    freq_map: Dict[str, int] = {}
    for s in stringList:
        freq_map[s] = freq_map.get(s, 0) + 1

    # Step 2: Map queries to their frequencies
    # This is O(m) time complexity and preserves exact order/duplicates
    return [freq_map.get(q, 0) for q in queries]

