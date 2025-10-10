"""
🧠 Interview Talking Points
Resizing logic: Doubles capacity when full

Time complexity:

append: amortized O(1)

get: O(1)

Space efficiency: Starts small, grows as needed

Edge cases: Handles out-of-bounds access
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
