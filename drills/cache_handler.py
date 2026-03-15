"""
## Problem Statement

Implement a time-limited cache handler that supports PUT/GET/DELETE/PATCH operations.
The cache must efficiently manage key-value pairs with optional expiration (TTL), return
appropriate status messages for each operation, and handle batch command execution. This
tests understanding of time management, lazy cleanup, and batch processing patterns.

## Whiteboard Coding Challenge Notes

* For this problem, I'm using a lazy cleanup strategy with timestamp-based expiration:

* **Ultra-Minimal One-Liner**:

  - Store key-value pairs with optional expiration timestamps; check/cleanup on access (lazy deletion) in O(1) per operation.

* **Complexity Analysis**:

  - **Time Complexity:** O(1) per operation (PUT, GET, DELETE, PATCH) with lazy expiration cleanup on access
  - **Space Complexity:** O(n) where n is the number of unexpired keys stored in the cache

## Algorithm Explanation

Lazy cleanup is the key design choice here. Rather than maintaining a background thread or
polling to remove expired entries, we check expiration only when a key is accessed. This avoids
the overhead of eager cleanup while keeping operations O(1).

* Key Concepts:

  - **Why lazy cleanup instead of eager cleanup?**
    Eager cleanup (background threads, heap of expirations) adds complexity and overhead for
    keys that are never accessed again. Lazy cleanup is simpler, requires no background processes,
    and amortizes cost naturally—only pay for cleanup when you actually use the cache.

  - **Why store (value, expiration_timestamp) tuples?**
    Storing expiration alongside the value eliminates separate lookups. A single tuple lookup
    tells us both the value AND whether it's expired. The None expiration represents "never expires."

  - **Why millisecond precision for time?**
    TTL parameters are given in milliseconds (interview standard), so all timestamps use milliseconds
    for consistency. The formula `now + duration` directly computes expiration without conversion errors.

  - **Why check expiration before operations?**
    The _get_unexpired_entry helper centralizes expiration logic. Every operation (GET, DELETE, PATCH)
    needs the same "is this key valid?" check. Centralizing this makes code maintainable and ensures
    consistent behavior across all operations.

## Algorithm Logic

1. **Initialization**: Store is a dictionary mapping key → (value, expiration_timestamp). Expiration is None if no TTL set.
2. **PUT operation**: Calculate expiration as current_time + duration, store (value, expiration) in dictionary.
3. **GET operation**: Check if key exists and isn't expired; perform lazy cleanup if expired; return value or "NOT FOUND".
4. **DELETE operation**: Verify key exists and isn't expired; remove from store if valid.
5. **PATCH operation**: Verify key exists and isn't expired; update expiration timestamp with new TTL.
6. **EXECUTE batch processing**: Parse command strings, validate format/arguments, invoke appropriate operation, collect results.

## Summary Variations

* **30-Second Pitch**:

  We implement a time-limited cache using a dictionary that stores (value, expiration_timestamp) tuples.
  The key insight is lazy cleanup—we only check expiration when a key is accessed, eliminating expensive
  background maintenance. PUT stores with an optional millisecond TTL, GET checks expiration and returns
  the value or "NOT FOUND", DELETE and PATCH verify the key exists before operating on it. The execute
  method parses batch commands and delegates to the appropriate operation, handling edge cases and
  invalid input gracefully.

* **Rapid-Fire Version**:

  - **Core idea**: Lazy cleanup (check expiration on access, not background)
  - **Data structure**: Dictionary of (value, expiration_timestamp) tuples
  - **Time handling**: All timestamps in milliseconds for consistency with TTL parameters
  - **Operations**: PUT (store with optional TTL), GET (return value or "NOT FOUND"), DELETE (verify then remove), PATCH (update TTL on existing key)
  - **Batch processing**: Parse commands, validate format, delegate to operations, collect results
  - **Edge cases**: Expired keys return "NOT FOUND", missing keys fail DELETE/PATCH, no-TTL keys never expire

## Use Cases

* Interview caching systems (Redis-like behavior at minimal scale)
* Time-based resource expiration (session tokens, temporary credentials)
* Cache eviction strategies (TTL is one of many eviction policies)
* API rate limiting (track request timestamps with expiration)
* Distributed system design (understanding staleness and TTL concepts)
"""

import time
from typing import Any, Dict, List, Optional, Tuple


class CacheHandler:
    """
    A time-limited cache handler that supports PUT/GET/DELETE/PATCH operations.

    Features:
    - PUT: Store a key-value pair with optional TTL (duration in milliseconds)
    - GET: Retrieve a value by key, returns "NOT FOUND" if expired or missing
    - DELETE: Remove a key, returns "ACCEPTED" or "NOT FOUND"
    - PATCH: Set/update TTL on an existing key, returns "ACCEPTED" or "NOT FOUND"
    - execute(): Batch process commands and return results
    - count(): Return number of unexpired keys

    Keys without duration parameter never expire.
    """

    def __init__(self) -> None:
        # key -> (value, expiration_timestamp or None)
        self.store: Dict[str, Tuple[Any, Optional[float]]] = {}

    def _get_unexpired_entry(self, key: str) -> Optional[Tuple[Any, Optional[float]]]:
        """
        Return (value, expiration) for a key only if it exists and isn't expired.
        Performs lazy cleanup by deleting the key if expired.
        
        Args:
            key: The cache key to check
            
        Returns:
            (value, expiration) tuple if key exists and is unexpired, else None
        """
        if key not in self.store:
            return None

        value, exp = self.store[key]
        
        # Key with no expiration is always valid
        if exp is None:
            return value, exp
        
        # Check if expired
        now = time.time() * 1000
        if exp <= now:
            del self.store[key]
            return None
        
        return value, exp

    def put(self, key: str, value: Any, duration: Optional[int] = None) -> str:
        """
        Store a key-value pair with optional TTL.

        Args:
            key: The cache key
            value: The value to store
            duration: Time to live in milliseconds (None for no expiration)

        Returns:
            "ACCEPTED"
        """
        exp_time = None
        if duration is not None:
            now = time.time() * 1000
            exp_time = now + duration

        self.store[key] = (value, exp_time)
        return "ACCEPTED"

    def get(self, key: str) -> Any:
        """
        Retrieve a value by key.

        Args:
            key: The cache key

        Returns:
            The value if key exists and not expired, else "NOT FOUND"
        """
        entry = self._get_unexpired_entry(key)
        if entry is None:
            return "NOT FOUND"

        value, _ = entry
        return value

    def delete(self, key: str) -> str:
        """
        Remove a key from cache.

        Args:
            key: The cache key

        Returns:
            "ACCEPTED" if key was deleted, "NOT FOUND" if key doesn't exist or is expired
        """
        if self._get_unexpired_entry(key) is None:
            return "NOT FOUND"

        del self.store[key]
        return "ACCEPTED"

    def patch(self, key: str, ttl: int) -> str:
        """
        Set or update TTL on an existing key.

        Args:
            key: The cache key
            ttl: New time to live in milliseconds

        Returns:
            "ACCEPTED" if TTL was set, "NOT FOUND" if key doesn't exist or is expired
        """
        entry = self._get_unexpired_entry(key)
        if entry is None:
            return "NOT FOUND"

        value, _ = entry
        now = time.time() * 1000
        exp_time = now + ttl
        self.store[key] = (value, exp_time)
        return "ACCEPTED"

    def count(self) -> int:
        """
        Count unexpired keys in the cache.

        Returns:
            Number of unexpired keys
        """
        return len(self.store)

    def execute(self, commands: List[str]) -> List[str]:
        """
        Execute a batch of commands and return results.

        Supported commands:
        - PUT key value [duration]: Store a key-value pair with optional duration
        - GET key: Retrieve a value
        - DELETE key: Remove a key
        - PATCH key TTL=<duration>: Set TTL on existing key

        Args:
            commands: List of command strings

        Returns:
            List of results corresponding to each command
        """
        results = []

        for cmd in commands:
            # Normalize whitespace around command tokens
            parts = cmd.split()
            if not parts:
                continue

            action = parts[0].upper()

            if action == "PUT":
                if len(parts) < 3:
                    results.append("INVALID COMMAND")
                    continue
                key = parts[1]
                value = parts[2]
                duration = None
                if len(parts) > 3:
                    try:
                        duration = int(parts[3])
                    except ValueError:
                        results.append("INVALID DURATION")
                        continue
                results.append(self.put(key, value, duration))

            elif action == "GET":
                if len(parts) < 2:
                    results.append("INVALID COMMAND")
                    continue
                key = parts[1]
                result = self.get(key)
                results.append(str(result))

            elif action == "DELETE":
                if len(parts) < 2:
                    results.append("INVALID COMMAND")
                    continue
                key = parts[1]
                results.append(self.delete(key))

            elif action == "PATCH":
                if len(parts) < 3:
                    results.append("INVALID COMMAND")
                    continue
                key = parts[1]
                ttl_part = parts[2]

                # Parse TTL=<duration> format
                if not ttl_part.startswith("TTL="):
                    results.append("INVALID TTL FORMAT")
                    continue

                try:
                    ttl = int(ttl_part[4:])  # Extract duration after "TTL="
                    results.append(self.patch(key, ttl))
                except ValueError:
                    results.append("INVALID TTL VALUE")

            else:
                results.append("UNKNOWN COMMAND")

        return results

