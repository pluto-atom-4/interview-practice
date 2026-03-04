"""
## Problem Statement

Given a string, return a new string where characters are sorted by their frequency in 
descending order. Characters with higher frequencies appear first. If multiple characters 
have the same frequency, their order doesn't matter. This tests frequency counting, sorting 
strategies, and string reconstruction—foundational skills for text processing and data analysis.

## Whiteboard Coding Challenge Notes

* For this problem, I'm using **Frequency Counting with Sorting**:

Rather than manually tracking character counts, I leverage the Counter utility for O(n) 
frequency counting, then sort the (character, frequency) pairs in descending order by frequency. 
This approach is straightforward, Pythonic, and efficient. The key insight is that sorting pairs 
naturally handles the grouping—all characters with the same frequency end up together, and we 
reconstruct the string by repeating each character according to its frequency.

* Key Concepts:

  - **Why use Counter instead of manually building a dictionary?**
  
    Counter is optimized for frequency counting, implemented in C, and handles edge cases 
    elegantly. Using the standard library reduces boilerplate and potential bugs. Since frequency 
    counting is a prerequisite to sorting, leveraging Counter lets us focus on the sorting logic 
    and string reconstruction, which are the core challenges of this problem.

  - **Why sort by negative frequency (or descending) instead of ascending?**
  
    We want high-frequency characters first in the output. Sorting by descending frequency means 
    the most common characters appear early. Using -x[1] (negating the count) in the sort key 
    achieves descending order with a min-heap mental model. Alternatively, we could use key=lambda 
    x: -x[1] or sorted(..., reverse=True, key=lambda x: x[1])—both work, but negation is concise.

  - **Why use a lambda function for the sort key?**
  
    The sorted() function by default compares tuples element-by-element. We need to sort by the 
    second element (frequency) instead of the first (character). A lambda extracts the frequency 
    and optionally negates it for descending order. This is Pythonic and clear: anyone reading 
    the code immediately understands we're sorting by frequency.

  - **Why use "".join() with a generator expression for string reconstruction?**
  
    string concatenation with + is O(n²) because each concatenation creates a new string object. 
    Using "".join() with an iterable is O(n) because Python concatenates all pieces at once. 
    A generator expression (ch * count for ch, count in sorted_chars) is memory-efficient—it 
    generates repeated characters on-the-fly without creating intermediate lists. This is both 
    fast and elegant.

  - **Why multiply the character by its count (ch * count) instead of looping?**
  
    In Python, "a" * 3 produces "aaa"—repeating strings is a built-in O(count) operation that's 
    highly optimized. A manual loop appending characters would be slower and less readable. This 
    conciseness is valued in interviews because it shows familiarity with Python idioms.

* **30-Second Pitch**:

I count the frequency of each character using Counter, then sort the character-frequency pairs 
in descending order by frequency. Once sorted, I reconstruct the string by repeating each 
character according to its count. This gives me an O(n) counting phase, O(k log k) sorting phase 
(where k is the number of unique characters), and O(n) reconstruction—overall O(n log k). For 
small character sets (like 26 letters), this is effectively O(n).

* **Rapid-Fire Version**:

- Use Counter to count character frequencies in O(n)
- Sort (character, frequency) pairs by frequency in descending order: O(k log k) where k = unique characters
- Reconstruct string by repeating each character count times: O(n)
- Use "".join() with generator for O(n) string building
- Total: O(n + k log k) time, O(k) space for Counter and sorted list
- For ASCII or Unicode, k is bounded, making this essentially O(n)

* **Ultra-Minimal One-Liner**:

- Count frequencies with Counter, sort by descending frequency, reconstruct via character repetition in O(n + k log k).

* **Complexity Analysis**:

- **Time Complexity:** O(n + k log k)
  - Counting: O(n) where n is the length of the input string
  - Sorting: O(k log k) where k is the number of unique characters
  - Reconstruction: O(n) to join the repeated characters
  - Overall: O(n + k log k). Since k ≤ 256 for extended ASCII or a constant for typical alphabets, 
    this is effectively O(n).
  
- **Space Complexity:** O(k)
  - Counter stores k unique characters and their frequencies
  - Sorted list stores the same k pairs
  - Output string is O(n), but this is the result, not auxiliary space
  - Dominated by O(k) where k is the number of unique characters

* **Use Cases**:

- **Data compression:** Identify and prioritize frequent characters for encoding (Huffman-like preprocessing)
- **Text analysis:** Identify most frequent letters for fingerprinting or language detection
- **Cache optimization:** Order cached items by access frequency for faster retrieval
- **UI/UX:** Display most-used features/emojis/words first based on user frequency data
- **Logging/monitoring:** Summarize logs with most frequent error codes or events
- **Natural language processing:** Analyze word or character frequency patterns for text classification

---

"""

from collections import Counter


def frequency_sort(s: str) -> str:
    freq = Counter(s)
    # Descending sort by frequency
    sorted_chars = sorted(freq.items(), key=lambda x: -x[1])

    return "".join(ch * count for ch, count in sorted_chars)
