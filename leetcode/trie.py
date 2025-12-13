def trie():
    """
    Trie Data Structure (Functional Implementation with Closures)
    ---------------------------------------------------------------
    A Trie (prefix tree) is a tree-based data structure that efficiently stores and retrieves strings.
    It is widely used in autocomplete, spell checking, IP routing, and prefix-based searching. This functional
    implementation uses closures and nested dictionaries to create a space-efficient representation without
    explicit class definitions. The Trie structure excels at operations involving string prefixes and is
    frequently asked in technical interviews to assess understanding of tree structures and string algorithms.

    Here is how the process works:

    1. **Trie Node Representation**: Use nested dictionaries for dynamic structure.
       - Each node is a dictionary with character keys and child node references
       - Special "#" key marks end-of-word (indicates a complete word stored in Trie)
       - Root node initialized with {"#": False} to handle empty prefix
       - Child nodes created on-demand using setdefault (lazy initialization)

    2. **Insert Operation**: Add a word character-by-character into the Trie.
       - Traverse from root node following the path of characters
       - For each character, create a new node if it doesn't exist (setdefault pattern)
       - After processing all characters, mark end-of-word by setting "#" to True
       - Time Complexity: O(m) where m = length of word being inserted
       - Space Complexity: O(m) in worst case if all characters create new nodes

    3. **Search Operation**: Find if a complete word exists in the Trie.
       - Start from root and traverse character by character
       - Return False immediately if any character path doesn't exist
       - After traversing all characters, check if "#" is True (marks word boundary)
       - Returns True only for complete words, not prefixes
       - Time Complexity: O(m) where m = length of word being searched
       - Space Complexity: O(1) for search operation (no extra data structures)

    4. **StartsWith Operation**: Check if any word with given prefix exists.
       - Similar to search but doesn't require end-of-word marker
       - Return True if we successfully traverse all prefix characters
       - Used for autocomplete: find all words starting with prefix
       - Time Complexity: O(p) where p = length of prefix
       - Space Complexity: O(1) for the operation itself

    5. **Closure Pattern**: Encapsulation of Trie state and operations.
       - Root dictionary is captured in closure and persistent across calls
       - Each operation function has access to root through closure
       - Returned dictionary exposes operations without modifying global state
       - Demonstrates functional programming patterns for data structure design

    6. **Node Creation Strategy**: Lazy initialization using setdefault.
       - Nodes only created when needed during insertion
       - Avoids pre-allocation of all 26 letters at every node (space efficient)
       - Pattern: node.setdefault(ch, {"#": False}) creates child if missing
       - Returns reference to child node (new or existing)

    Example: Building a Trie with words ["cat", "car", "dog"]
    - insert("cat"): root → 'c' → 'a' → 't' (mark # = True)
    - insert("car"): root → 'c' → 'a' → 'r' (mark # = True)
    - insert("dog"): root → 'd' → 'o' → 'g' (mark # = True)
    - search("cat"): True (word exists and # is True)
    - search("ca"): False (prefix exists but # is False)
    - startsWith("ca"): True (prefix path exists regardless of #)

    Time Complexity Summary:
    - insert(word): O(m) where m = word length
    - search(word): O(m) where m = word length
    - startsWith(prefix): O(p) where p = prefix length
    - All operations are linear in the string length (no backtracking)

    Space Complexity Summary:
    - Overall: O(ALPHABET_SIZE * N * M) where N = number of words, M = average length
    - For lowercase English: O(26 * N * M) which simplifies to O(N * M)
    - More efficient than storing strings separately (no character repetition)
    - Prefix sharing dramatically reduces space vs separate string storage

    Advantages of Trie:
    - Efficient prefix searching (autocomplete, spell check)
    - Space-efficient for large dictionaries (shared prefixes)
    - No hash function needed (unlike hash tables)
    - Lexicographic ordering built-in (tree traversal)
    - Deterministic performance (no hash collisions)

    Disadvantages of Trie:
    - Requires more memory for small dictionaries vs hash table
    - Slower for single word lookup vs hash table (hash constant factor)
    - Complex implementation compared to hash table
    - Cache-unfriendly (sparse tree structure)

    INTERVIEW CONTEXT:
    - Explain why Trie is used: prefix-based searching, autocomplete
    - Discuss space-time tradeoffs vs hash tables
    - Mention closed-form solutions using closures (functional programming)
    - Be ready for follow-ups: auto-delete unused nodes, word frequency tracking
    - Connect to practical use cases: phone book, URL routing, spell checker

    Key Interview Points:
    - "#" marker: how to distinguish prefix vs complete word
    - Lazy node creation: space efficiency optimization
    - Closure pattern: encapsulation without classes
    - Time complexity: always O(word_length), not O(log n) like trees
    - Space optimization: shared prefixes eliminate redundancy

    Common Follow-ups:
    - "How would you implement auto-delete?" Track node usage, garbage collect
    - "Support word frequencies?" Add count to "#" instead of boolean
    - "Find all words with prefix?" DFS/BFS from prefix node
    - "Implement using array of 26 pointers?" Trade space for speed
    - "What about non-English characters?" Use dictionary instead of fixed array

    This Trie implementation demonstrates understanding of:
    - Tree-based data structures for string problems
    - Space optimization through prefix sharing
    - Functional programming patterns (closures, no classes)
    - String algorithm fundamentals for interviews
    """

    root = {"#": False}  # '#' marks end-of-word

    def insert(word: str) -> None:
        node = root
        for ch in word:
            node = node.setdefault(ch, {"#": False})
        node["#"] = True

    def search(word: str) -> bool:
        node = root
        for ch in word:
            if ch not in node:
                return False
            node = node[ch]
        return node.get("#", False)

    def startsWith(prefix: str) -> bool:
        node = root
        for ch in prefix:
            if ch not in node:
                return False
            node = node[ch]
        return True

    # Decorator wrapper to expose operations
    def expose(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper

    return {
        "insert": expose(insert),
        "search": expose(search),
        "startsWith": expose(startsWith),
    }
