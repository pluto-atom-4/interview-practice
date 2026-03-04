"""
## Problem Statement

Group a list of strings into lists where each group contains anagrams. Two words are anagrams if they contain the same 
characters with the same frequencies. The goal is to return all groups of anagrams from the input, making this a crucial 
skill for understanding character frequency patterns and hash-based grouping in interviews.

## Whiteboard Coding Challenge Notes

* For this problem, I'm using **character frequency mapping with hash table grouping**:

Character frequency serves as a unique signature for anagrams. By converting each word's character frequency into a 
hashable key, we can group words with identical signatures efficiently using a hash table.

* Key Concepts:

  - **Why use character frequency as a grouping key?**
  Anagrams by definition have identical character frequencies. Two words are anagrams if and only if they have the same 
  count of each character. This makes frequency tuples a perfect hash key for grouping—words with identical frequencies 
  map to the same key, automatically collecting anagrams together.

  - **Why represent frequency as a list of 26 counts?**
  For lowercase English letters, a fixed-size array of 26 elements (one per letter a-z) is optimal. We use `ord(ch) - ord("a")` 
  to map each character to its index (a→0, b→1, ..., z→25). This avoids the overhead of dictionaries and allows conversion 
  to a hashable tuple for use as a hash key. Alternative: sorting characters (e.g., "aabbc" → "aabbc") works but is O(n log n) 
  per word versus O(n) for frequency counting.

  - **Why convert the frequency list to a tuple?**
  Lists are not hashable in Python and cannot be used as dictionary keys. Converting to a tuple makes it hashable while 
  preserving the frequency information. This enables grouping words with identical frequency profiles into the same bucket 
  in the defaultdict.

* **30-Second Pitch**:

Group anagrams by treating character frequency signatures as hash keys. For each word, count how many times each letter 
appears (a frequency array of 26 values). Convert this array to a hashable tuple and use it as a key in a defaultdict. 
All words with the same letter frequencies automatically group together under the same key. Finally, return all groups 
as lists of values. Time is O(n*k) where n is word count and k is average word length, space is O(n*k) for storage.

* **Ultra-Minimal One-Liner**:

- Use character frequency tuples as hash keys to group anagrams in O(n*k) time and space.

* **Complexity Analysis**:

- **Time Complexity:** O(n*k) where n is the number of strings and k is the maximum length of a string. Each word requires 
  O(k) work to count character frequencies, and we process n words total.
- **Space Complexity:** O(n*k) for storing all strings in the hash table and groupings. The defaultdict and its values 
  collectively hold all input data.

* **Use Cases**:

Anagram grouping is foundational in linguistics, cryptography, and text analysis. It appears in spell-checking systems 
(finding similar words), deduplication tasks, and document clustering where semantically related content needs grouping. 
This approach generalizes to any scenario where items share a common signature or fingerprint.
"""

from collections import defaultdict
from typing import List


def group_anagrams(strs: List[str]) -> List[List[str]]:

    groups = defaultdict(list)

    for word in strs:
        freq = [0] * 26 # assuming the word is composed in lower cse alphabets
        for ch in word:
            freq[ord(ch) - ord("a")] += 1 # alphabets table

        groups[tuple(freq)].append(word)

    return list(groups.values())
