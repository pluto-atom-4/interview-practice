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

    def _is_expired(self, key: str) -> bool:
        """Check if a key has expired."""
        if key not in self.store:
            return False

        _, exp = self.store[key]
        if exp is None:
            return False

        now = time.time() * 1000
        return exp <= now

    def _cleanup_expired(self, key: str) -> None:
        """Remove key if it has expired."""
        if self._is_expired(key):
            del self.store[key]

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
        if key not in self.store:
            return "NOT FOUND"

        if self._is_expired(key):
            self._cleanup_expired(key)
            return "NOT FOUND"

        value, _ = self.store[key]
        return value

    def delete(self, key: str) -> str:
        """
        Remove a key from cache.

        Args:
            key: The cache key

        Returns:
            "ACCEPTED" if key was deleted, "NOT FOUND" if key doesn't exist or is expired
        """
        if key not in self.store or self._is_expired(key):
            self._cleanup_expired(key)
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
        if key not in self.store or self._is_expired(key):
            self._cleanup_expired(key)
            return "NOT FOUND"

        value, _ = self.store[key]
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
        now = time.time() * 1000
        expired_keys = []

        for key, (_, exp) in self.store.items():
            if exp is not None and exp <= now:
                expired_keys.append(key)

        for key in expired_keys:
            del self.store[key]

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
                    continue

            else:
                results.append("UNKNOWN COMMAND")

        return results

