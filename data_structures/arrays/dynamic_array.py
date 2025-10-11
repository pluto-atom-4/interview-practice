"""
Dynamic Array Data Structure Explained Step-by-Step
-------------------------------------------------
A dynamic array is a resizable array that automatically grows when more space is needed, providing the flexibility of lists with efficient random access.

Here is how the process works:

1. **Initialization**: Start with a small fixed capacity (typically 1) and track both size and capacity.
   - Size: number of elements currently stored
   - Capacity: total space available in the underlying array

2. **Append**: Add elements to the end of the array.
   - If there's space, simply add the element
   - If the array is full, double the capacity and copy all elements to the new array
   - This doubling strategy ensures amortized O(1) performance

3. **Insert**: Add an element at any valid index.
   - Shift all elements from that index to the right
   - Resize if necessary before insertion

4. **Remove**: Find and delete the first occurrence of a value.
   - Locate the element by linear search
   - Shift all elements after it to the left to fill the gap
   - Decrease the size counter

5. **Access (Get)**: Retrieve element at any index with bounds checking.
   - Direct array access provides O(1) performance
   - Validate index is within bounds before access

Key advantages:
- Amortized O(1) append operations due to doubling strategy
- O(1) random access like static arrays
- Automatic memory management

Time Complexity:
- Append: O(1) amortized, O(n) worst case (during resize)
- Insert: O(n) due to shifting elements
- Remove: O(n) due to search and shifting
- Get: O(1) direct access

This data structure demonstrates important concepts like amortized analysis, memory management,
and trade-offs between time and space efficiency, commonly discussed in technical interviews.
"""


class DynamicArray:
    def __init__(self):
        self.capacity = 1
        self.size = 0
        self.array = self._make_array(self.capacity)

    def _make_array(self, new_capacity):
        return [None] * new_capacity

    def _resize(self, new_capacity):
        new_array = self._make_array(new_capacity)
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def append(self, value):
        if self.size == self.capacity:
            self._resize(2 * self.capacity)
        self.array[self.size] = value
        self.size += 1

    def insert(self, index, value):
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")
        if self.size == self.capacity:
            self._resize(2 * self.capacity)
        for i in range(self.size, index, -1):
            self.array[i] = self.array[i - 1]
        self.array[index] = value
        self.size += 1

    def remove(self, value):
        for i in range(self.size):
            if self.array[i] == value:
                for j in range(i, self.size - 1):
                    self.array[j] = self.array[j + 1]
                self.array[self.size - 1] = None
                self.size -= 1
                return
        raise ValueError("Value not found")

    def get(self, index):
        if 0 <= index < self.size:
            return self.array[index]
        raise IndexError("Index out of bounds")

    def __str__(self):
        return "[" + ", ".join(str(self.array[i]) for i in range(self.size)) + "]"
