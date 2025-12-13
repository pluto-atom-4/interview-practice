from typing import Dict, Union


def make_trie():
    """
    Trie Data Structure (Singledispatch/Registry Pattern Implementation)
    -----------------------------------------------------------------------
    This is an advanced functional implementation of a Trie using a dispatcher/registry pattern
    instead of closures. The singledispatch-like pattern allows operations to be registered dynamically
    while maintaining clean separation of concerns. This implementation demonstrates advanced design patterns
    and is useful for showing understanding of functional programming, decorator patterns, and extensible
    architectures. The registry pattern is common in real-world systems for plugin systems and operation handlers.

    Here is how the process works:

    1. **Root Node Initialization**: Create the Trie root with end-of-word marker.
       - trie dictionary serves as root node: {"#": False}
       - "#" key marks the end of a word (boolean flag for word boundaries)
       - Initially empty trie has only root with no words stored
       - Type hint: Dict[str, Union[bool, Dict]] shows recursive structure

    2. **Decorator Registration Pattern**: Dynamic operation registration mechanism.
       - define register(name): creates a decorator for operation functions
       - Decorator wrapper stores function in operations dictionary by name
       - Allows registering operations after function definition
       - Similar to @register("insert"), @register("search") pattern
       - More flexible than hard-coded methods in classes

    3. **Insert Operation**: Add words to Trie with registered operation.
       - @register("insert") decorator registers insert function
       - Traverse Trie from root, creating nodes as needed
       - Use setdefault(ch, {"#": False}) for lazy node creation
       - Set node["#"] = True after processing all characters
       - Returns True to indicate successful insertion

    4. **Search Operation**: Find complete words in Trie with registered operation.
       - @register("search") decorator registers search function
       - Traverse character-by-character from root
       - Return False if any character doesn't exist in path
       - Check node.get("#", False) to verify word boundary
       - Only returns True for complete words, not prefixes

    5. **StartsWith Operation**: Check prefix existence with registered operation.
       - @register("startsWith") decorator registers startswith function
       - Similar traversal to search but ignores "#" marker
       - Returns True if prefix path exists (regardless of word boundary)
       - Used for autocomplete and prefix-based searching
       - Time complexity O(p) where p = prefix length

    6. **Public API Exposure**: Return operations through dictionary interface.
       - Operations dictionary built through decoration process
       - Final return statement exposes clean interface:
         {"insert": operation, "search": operation, "startsWith": operation}
       - Caller uses: trie_ops = make_trie(); trie_ops["insert"]("word")
       - Encapsulates internal structure and operation registry

    Example Usage:
    ```
    trie_ops = make_trie()
    trie_ops["insert"]("apple")
    trie_ops["insert"]("app")
    trie_ops["search"]("apple")      # True
    trie_ops["search"]("app")        # True
    trie_ops["search"]("appl")       # False (prefix, not complete word)
    trie_ops["startsWith"]("app")    # True
    trie_ops["startsWith"]("appl")   # True
    ```

    Time Complexity Summary:
    - insert(word): O(m) where m = word length
    - search(word): O(m) where m = word length
    - startsWith(prefix): O(p) where p = prefix length

    Space Complexity Summary:
    - Storage: O(ALPHABET_SIZE * N * M) for N words with average length M
    - Dictionary overhead: Python dictionaries use hash tables internally
    - Prefix sharing reduces duplication compared to separate string storage

    Advanced Pattern Concepts Demonstrated:

    1. **Registry Pattern**: Operations registered through decorators
       - Similar to plugin systems and extension frameworks
       - Allows dynamic operation registration
       - Common in real-world architectures (Django, Flask)
       - More extensible than direct class methods

    2. **Closure with Dispatcher**: Trie state captured in closure, operations in registry
       - Root node accessible to all registered operations
       - Operations dictionary provides indirection layer
       - Separates data (trie) from operations (registry)
       - Clean interface without exposing internal structure

    3. **Functional Composition**: Building complex behavior from simple functions
       - Each operation (insert, search, startswith) is independent function
       - Decorator pattern glues them together
       - Can compose and modify operations without changing core data structure

    INTERVIEW CONTEXT:
    - Demonstrates advanced pattern knowledge (registry/dispatcher)
    - Shows understanding of functional programming and decorators
    - Discusses design patterns beyond basic implementations
    - Practical relevance to plugin systems and extensible architectures
    - Can explain trade-offs: registry pattern vs direct methods

    Key Interview Points:
    - Registry Pattern: how operations are dynamically registered
    - Decorator Pattern: how @register works to build operation dictionary
    - Closure Pattern: how trie and operations captured in function scope
    - Functional vs OOP: benefits and trade-offs compared to class-based Trie
    - Extensibility: how new operations can be added without modifying existing code

    Comparison: Closure vs Registry vs Class Implementation

    Closure (trie.py):
    - Simple, direct approach
    - Each call to trie() creates new Trie instance
    - Good for basic use cases

    Registry (trie_singledispatch.py):
    - Advanced pattern demonstration
    - Decorator-based operation registration
    - Shows architecture design knowledge
    - Extensible for new operations

    Class-based:
    - Traditional OOP approach
    - Clear method definitions
    - Easier for beginners
    - More verbose

    Common Follow-ups to Expect:
    - "How would you add a delete operation?" Add @register("delete") function
    - "How to support word frequencies?" Modify "#" to store count instead of boolean
    - "Performance optimization?" Use array instead of dictionary for 26 letters
    - "How is this different from closure version?" Registry pattern vs direct return
    - "Use cases for registry pattern?" Plugin systems, event handlers, middleware

    This advanced implementation demonstrates mastery of:
    - Trie data structure fundamentals
    - Design patterns (registry, decorator, factory)
    - Functional programming with closures and higher-order functions
    - Creating extensible and maintainable code architectures
    - Pattern selection based on use case requirements
    """

    trie: Dict[str, Union[bool, Dict]] = {"#": False}  # root node

    # Define operations as a dictionary of callables
    operations = {}

    # Register decorator to add operations
    def register(name):
        def decorator(func):
            operations[name] = func
            return func
        return decorator

    # -----------------------------
    # INSERT
    # -----------------------------
    @register("insert")
    def insert(word: str):
        node = trie
        for ch in word:
            node = node.setdefault(ch, {"#": False})
        node["#"] = True
        return True

    # -----------------------------
    # SEARCH
    # -----------------------------
    @register("search")
    def search(word: str):
        node = trie
        for ch in word:
            if ch not in node:
                return False
            node = node[ch]
        return node.get("#", False)

    # -----------------------------
    # STARTSWITH
    # -----------------------------
    @register("startsWith")
    def startswith(prefix: str):
        node = trie
        for ch in prefix:
            if ch not in node:
                return False
            node = node[ch]
        return True

    # -----------------------------
    # Public API
    # -----------------------------
    return {
        "insert": operations["insert"],
        "search": operations["search"],
        "startsWith": operations["startsWith"],
    }
