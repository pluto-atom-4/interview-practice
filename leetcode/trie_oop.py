"""
## Problem Statement

Implement a Trie (prefix tree) data structure that supports efficient insertion, exact word 
search, and prefix matching. The goal is to enable fast string lookups and auto-completion 
by organizing strings in a tree where each path from root to node represents a prefix. 
This tests understanding of hierarchical data structures, OOP design, and space-time trade-offs.

## Whiteboard Coding Challenge Notes

* For this problem, I'm using **Trie (Prefix Tree) with OOP Design**:

A Trie organizes strings hierarchically, storing characters as nodes and using an is_end 
flag to distinguish complete words from prefixes. This enables O(m) search/insert time 
(where m is word length, independent of word count) and efficient prefix matching. The 
OOP approach separates concerns: TrieNode handles structure, Trie class handles operations, 
making code maintainable and extensible.

* Key Concepts:

  - **Why use a Trie instead of a HashSet or sorted list?**
  
    A Trie excels at prefix matching and auto-completion. HashSet is O(1) for exact lookup 
    but can't efficiently find all words starting with a prefix. A sorted list enables binary 
    search but modifying it is expensive. A Trie is O(m) for search (m = word length, not 
    word count), and prefix queries are naturally efficient. For applications like search 
    suggestions, IP routing tables, or spell-checking, Trie is superior.

  - **Why use is_end flag instead of storing None or marking nodes differently?**
  
    The is_end boolean clearly separates complete words from intermediate prefixes. This allows 
    "cat" and "cats" to coexist: "cat" has is_end=True at that node, while "cats" continues 
    from there. Using None would lose the prefix path. The boolean flag is explicit, efficient 
    (single bit conceptually), and makes the code's intent crystal clear.

  - **Why separate search() and starts_with() instead of a single lookup method?**
  
    These methods serve different use cases. search(word) checks if a complete word exists 
    (requires is_end=True), while starts_with(prefix) checks if any word begins with the prefix 
    (only checks path existence). Separating them clarifies intent and prevents logic errors. 
    For example, search("car") returns False for a Trie with only "carpet", but starts_with 
    ("car") returns True. This separation is essential for applications like autocomplete.

  - **Why use _find_node() as a helper method?**
  
    Finding a node by traversing characters is a core operation used by both search() and 
    starts_with(). Extracting it into a private method (convention: _prefix) eliminates code 
    duplication, centralizes the traversal logic (easier to debug or optimize), and makes the 
    public methods concise and readable. It also simplifies prefix-based queries if you later 
    need to find all words starting with a prefix.

  - **Why use dataclass for TrieNode with default_factory for children?**
  
    Dataclass reduces boilerplate (no __init__ needed) and makes the data structure clear. 
    Using default_factory=dict ensures each TrieNode instance gets its own dictionary, avoiding 
    the classic Python gotcha of mutable default arguments shared across instances. This is both 
    safe and readable, demonstrating clean OOP design in interviews.

* **30-Second Pitch**:

I implement a Trie using an OOP approach where each TrieNode stores a dictionary of child 
nodes and an is_end flag marking complete words. The root starts empty, and I insert words 
by traversing or creating nodes character-by-character. For search, I traverse following the 
word and check if is_end is true at the end. For prefix matching, I just check if the 
traversal path exists, regardless of is_end. This gives me O(m) operations where m is the 
word/prefix length, which is efficient for applications like auto-completion.

* **Rapid-Fire Version**:

- Trie: hierarchical structure storing characters as nodes in a tree
- TrieNode: stores children (dict) and is_end (bool) flag using dataclass
- insert(word): traverse or create nodes per character, mark is_end=True at completion
- search(word): traverse and return is_end value at the end node (or False if path doesn't exist)
- starts_with(prefix): traverse and return True if path exists (ignore is_end)
- Time: O(m) for insert/search/prefix where m = word/prefix length (independent of word count!)
- Space: O(ALPHABET_SIZE * N * M) for N words of average length M

* **Ultra-Minimal One-Liner**:

- Hierarchical string storage with O(m) search/insert via character-by-character tree traversal with end-of-word flags.

* **Complexity Analysis**:

- **Time Complexity:** O(m) for insert, search, and starts_with operations
  - m is the length of the word or prefix being processed
  - Independent of the number of words already in the Trie, making it highly efficient for large datasets
  - Each character traversal is O(1) dictionary lookup, done m times
  
- **Space Complexity:** O(ALPHABET_SIZE * N * M) in the worst case
  - ALPHABET_SIZE: unique characters possible (26 for lowercase English, ~128 for ASCII)
  - N: number of unique words stored
  - M: average word length
  - Each node stores a dictionary of children; in worst case (no shared prefixes), space grows with 
    the sum of all word lengths multiplied by alphabet size
  - With common prefixes, space is significantly better due to sharing

* **Use Cases and Transferability**:

- **Autocomplete systems:** Efficiently find all words starting with a user's typed prefix
- **Spell checking:** Quickly verify words against a dictionary
- **IP routing tables:** Route packets using longest-prefix matching
- **Phone directories:** Search by name prefix without full name
- **Search suggestions:** Real-time prefix-based filtering
- **String manipulation and uniqueness checks:** A Trie naturally handles **name uniqueness and ranking 
  in lists** by organizing similar names hierarchically. Just as the Trie uses a sliding window of 
  characters to identify shared prefixes, you can apply the same prefix-extraction logic to identify 
  name duplicates or variations in user lists (e.g., "John" vs "John_Admin"). This transferability 
  extends to any domain where hierarchical prefix matching applies: DNS names, package namespaces, 
  user hierarchies, or taxonomy systems. The core pattern—organize strings by shared prefixes, then 
  query efficiently—solves uniqueness verification and ranking problems where names must be 
  disambiguated or prioritized by their hierarchical relationship.

---

"""

from dataclasses import dataclass, field
from typing import Dict

@dataclass
class TrieNode:
    children: Dict[str, "TrieNode"] = field(default_factory=dict)
    is_end: bool = False


class Trie:
    def __init__(self)-> None:
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end =True

    def search(self, word: str) -> bool:
        node = self._find_node(word)
        return node.is_end if node else False

    def starts_with(self, prefix: str)-> bool:
        return self._find_node(prefix) is not None

    def _find_node(self, s: str) -> TrieNode | None :
        node = self.root
        for ch in s:
            if ch not in node.children:
                return None
            node = node.children[ch]
        return node
