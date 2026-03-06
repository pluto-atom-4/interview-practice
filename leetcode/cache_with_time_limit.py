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
