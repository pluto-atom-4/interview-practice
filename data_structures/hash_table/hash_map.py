"""
Hash Map (Hash Table) Data Structure Explained Step-by-Step
-----------------------------------------------------------
A Hash Map, also known as Hash Table, is a fundamental data structure that provides efficient key-value
storage and retrieval. It uses a hash function to map keys to indices in an underlying array, enabling
average O(1) time complexity for basic operations. Hash Maps are essential for caching, database indexing,
symbol tables, and implementing other data structures like sets and dictionaries.

Here is how the process works:

1. **Hash Function**: Convert keys into array indices using a hash function.
   - Uses Python's built-in hash() function to compute hash value
   - Applies modulo operation (hash(key) % size) to fit within array bounds
   - Ensures uniform distribution of keys across available buckets
   - Same key always produces the same index for consistent access

2. **Collision Handling**: Manage situations where different keys hash to the same index.
   - Uses separate chaining with lists to store multiple key-value pairs per bucket
   - Each bucket is a list that can hold multiple (key, value) tuples
   - When collision occurs, new pairs are appended to the existing bucket list
   - Linear search within bucket to find specific key-value pairs

3. **Put Operation**: Insert or update key-value pairs in the hash map.
   - Compute hash index for the given key using hash function
   - Search the bucket at that index for existing key
   - If key exists, update its value in place (overwrite)
   - If key doesn't exist, append new (key, value) tuple to bucket

4. **Get Operation**: Retrieve value associated with a given key.
   - Compute hash index for the key using same hash function
   - Search through the bucket list at that index
   - Linear scan comparing keys until match is found
   - Return associated value or raise KeyError if key not found

5. **Remove Operation**: Delete key-value pair from the hash map.
   - Compute hash index and locate the appropriate bucket
   - Search bucket list for the key to be removed
   - Remove the (key, value) tuple from the list when found
   - Raise KeyError if key doesn't exist in the hash map

6. **Contains Operation**: Check if a key exists in the hash map.
   - Compute hash index and access the corresponding bucket
   - Use any() function to efficiently check if key exists in bucket
   - Return boolean result without exposing internal structure
   - Provides membership testing without value retrieval

Example: Storing key="name", value="John"
- Hash computation: hash("name") % 100 = 85 (assuming size=100)
- Process: Access bucket[85], check for existing "name", append or update
- Result: Fast O(1) average access to retrieve "John" when querying "name"

Time Complexity: O(1) average for all operations (O(n) worst case with many collisions)
Space Complexity: O(n) where n is the number of key-value pairs stored
Load Factor: Ratio of stored elements to total buckets affects performance

This implementation demonstrates fundamental hashing concepts and is essential for
understanding database indexing, caching systems, and efficient data retrieval patterns.
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
