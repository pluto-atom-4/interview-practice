"""
## Problem Statement

Design a time-limited cache that stores key-value pairs with expiration times. Each entry expires 
after a specified duration (in milliseconds). The cache must support get (retrieve unexpired value), 
set (store or update with new expiration), and count (return number of unexpired entries) operations 
while automatically cleaning up expired entries. This tests understanding of expiration tracking, 
lazy deletion, and timestamp-based state management.

## Whiteboard Coding Challenge Notes

* For this problem, I'm using a **lazy deletion with timestamp-based expiration** approach:

* **Ultra-Minimal One-Liner**:

- Store (value, expiration_timestamp) tuples and check expiration on each access, deleting lazily when detected.

* **Complexity Analysis**:

- **Time Complexity:** O(1) for set/get operations, O(n) for count (must scan all entries to clean expired ones)
- **Space Complexity:** O(n) where n is the number of cached entries (stores key, value, and timestamp for each)

## Algorithm Explanation

The key insight is that expiration is a **lazy operation**—we don't need a background process or heap to 
track expiration times. Instead, we check timestamps only when entries are accessed. This eliminates 
the overhead of maintaining a priority queue or timer while keeping get/set efficient.

* Key Concepts:

  - **Timestamp-Based Expiration**: Why/How?
  
    Convert current time to milliseconds (`time.time() * 1000`) and store expiration as `now + duration`. 
    This avoids floating-point precision issues and aligns with the millisecond duration parameter. 
    When accessed, compare current time against the stored expiration timestamp to determine validity.

  - **Lazy Deletion**: Why/How?
  
    Don't delete entries until accessed or counted. This is efficient because most keys may never be 
    accessed again after expiration. Only the set, get, and count operations trigger cleanup checks, 
    reducing unnecessary work compared to eager cleanup with background timers or heaps.

  - **Return Value for set()**: Why/How?
  
    Return True only if the key existed AND was not yet expired before updating. This lets callers 
    distinguish between "replaced valid entry" (True) and "new key or already expired" (False). 
    Always overwrite the entry regardless, so old expiration times don't cause stale data.

## Algorithm Logic

1. **Set operation**: Check if key exists and is unexpired (by comparing stored expiration against current time). Update the entry with new value and new expiration timestamp. Return True only if key was valid before the update.

2. **Get operation**: Return -1 if key doesn't exist. Check if stored expiration ≤ current time; if expired, delete and return -1. Otherwise return the value.

3. **Count operation**: Scan all entries, identify and delete those with expiration ≤ current time. Return the count of remaining valid entries.

## Summary Variations

* **30-Second Pitch**:

We implement a cache where each key-value pair has an expiration timestamp. When a key is accessed via get, 
we check if its expiration has passed; if so, we delete it and return -1. For set, we update the entry with 
a new expiration time and return whether it was valid before updating. For count, we scan and clean all 
expired entries, returning the valid count. No background cleanup is needed—expiration is checked lazily on 
access, making it efficient and simple.

* **Rapid-Fire Version**:

- Store entries as (value, expiration_timestamp) tuples in a dictionary
- Lazy deletion: only check/clean expiration on access, not proactively
- set() returns True only if key existed and hadn't expired yet
- get() returns -1 for missing or expired keys; deletes on expiration
- count() scans and removes all expired entries, returns valid count
- Time: O(1) set/get, O(n) count; Space: O(n)

## Use Cases

This pattern is used in real-world caching (Redis with TTL), session management (expiring authentication tokens), 
temporary data storage (API rate-limit buckets), and any scenario where entries need automatic lifecycle 
management without explicit deletion requests.
"""

import time
from typing import Any, Dict, Tuple


class TimeLimitedCache:
    """
    A cache where each key expires after a given duration (in milliseconds).

    Methods:
    - set(key, value, duration): returns True if key already existed and unexpired.
    - get(key): returns value if unexpired, else -1.
    - count(): returns number of unexpired keys.
    """

    def __init__(self) -> None:
        # key -> (value, expiration_timestamp)
        self.store: Dict[int, Tuple[Any, float]] = {}

    def set(self, key: int, value: Any, duration: int) -> bool:
        now = time.time() * 1000
        existed_and_valid = False

        if key in self.store:
            _, exp = self.store[key]
            if exp > now:
                existed_and_valid = True

        self.store[key] = (value, now + duration)
        return existed_and_valid

    def get(self, key: int) -> Any:
        now = time.time() * 1000
        if key not in self.store:
            return -1

        value, exp = self.store[key]
        if exp <= now:
            del self.store[key]
            return -1

        return value

    def count(self) -> int:
        now = time.time() * 1000
        expired_keys = [k for k, (_, exp) in self.store.items() if exp <= now]

        for k in expired_keys:
            del self.store[k]

        return len(self.store)
