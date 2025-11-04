"""
Hash Map — one of the most popular and powerful data structures used in caching, indexing, and fast lookups.
"""

class HashMap:
    def __init__(self, size=100):
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        index = self._hash(key)
        bucket = self.buckets[index]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))

    def get(self, key):
        index = self._hash(key)
        bucket = self.buckets[index]
        for k, v in bucket:
            if k == key:
                return v
        raise KeyError(f"Key '{key}' not found")

    def remove(self, key):
        index = self._hash(key)
        bucket = self.buckets[index]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return
        raise KeyError(f"Key '{key}' not found")

    def contains(self, key):
        index = self._hash(key)
        bucket = self.buckets[index]
        return any(k == key for k, _ in bucket)
