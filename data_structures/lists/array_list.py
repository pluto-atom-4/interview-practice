class ArrayList:
    """A dynamic array implementation similar to Python's list."""

    def __init__(self, capacity=4):
        self._capacity = max(4, capacity)
        self._size = 0
        self._data = [None] * self._capacity
        self._initial_capacity = self._capacity  # Track initial capacity
        self._max_capacity = self._capacity  # Track maximum capacity reached
        self._max_size = 0  # Track maximum size reached
        self._ever_full = False  # Track if array has ever been filled to capacity

    # ------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------

    def _resize(self, new_capacity):
        new_capacity = max(4, new_capacity)  # never shrink below 4
        new_data = [None] * new_capacity

        for i in range(self._size):
            new_data[i] = self._data[i]

        self._data = new_data
        self._capacity = new_capacity
        # Track maximum capacity reached
        if new_capacity > self._max_capacity:
            self._max_capacity = new_capacity

    def _check_bounds(self, index):
        if index < 0 or index >= self._size:
            raise IndexError("index out of range")

    def _maybe_shrink(self):
        """
        Shrink when size reaches a threshold based on capacity.
        Only shrink if: capacity grew OR (initial_capacity > 4 AND max_size >= half of initial).
        - For capacity <= 8: shrink when size <= capacity // 2
        - For capacity > 8: shrink when size <= capacity // 4
        """
        # Shrink if:
        # 1. Capacity was grown through doubling, OR
        # 2. Initial capacity > 4 AND max_size >= half of initial_capacity (used at least 50%)
        capacity_grew = self._max_capacity > self._initial_capacity
        capacity_well_used = self._initial_capacity > 4 and self._max_size * 2 >= self._initial_capacity

        if not (capacity_grew or capacity_well_used):
            return

        if self._capacity <= 8:
            threshold = self._capacity // 2
        else:
            threshold = self._capacity // 4

        if self._size <= threshold and self._capacity > 4:
            self._resize(self._capacity // 2)

    # ------------------------------------------------------------
    # Core operations
    # ------------------------------------------------------------

    def append(self, value):
        if self._size == self._capacity:
            self._resize(self._capacity * 2)
        self._data[self._size] = value
        self._size += 1
        # Track maximum size reached
        if self._size > self._max_size:
            self._max_size = self._size
        # Mark if we've ever filled the capacity
        if self._size == self._capacity:
            self._ever_full = True

    def prepend(self, value):
        self.insert(0, value)

    def insert(self, index, value):
        if index < 0 or index > self._size:
            raise IndexError("index out of range")

        if self._size == self._capacity:
            self._resize(self._capacity * 2)

        for i in range(self._size, index, -1):
            self._data[i] = self._data[i - 1]

        self._data[index] = value
        self._size += 1
        # Mark if we've ever filled the capacity
        if self._size == self._capacity:
            self._ever_full = True

    def delete(self, index):
        self._check_bounds(index)

        for i in range(index, self._size - 1):
            self._data[i] = self._data[i + 1]

        self._data[self._size - 1] = None
        self._size -= 1

        self._maybe_shrink()

    def concatenate(self, other):
        if isinstance(other, ArrayList):
            other = other.to_array()

        for item in other:
            self.append(item)

    def sort(self):
        arr = self.to_array()
        arr.sort()
        self._data = arr + [None] * (self._capacity - len(arr))
        self._size = len(arr)

    def set_size(self, new_size):
        if new_size < 0:
            raise ValueError("size cannot be negative")

        if new_size > self._capacity:
            self._resize(max(new_size, self._capacity * 2))

        if new_size > self._size:
            for i in range(self._size, new_size):
                self._data[i] = None

        self._size = new_size
        self._maybe_shrink()

    def extend_capacity(self, new_capacity):
        if new_capacity > self._capacity:
            self._resize(new_capacity)

    def to_array(self):
        return [self._data[i] for i in range(self._size)]

    # ------------------------------------------------------------
    # Pythonic helpers
    # ------------------------------------------------------------

    def __len__(self):
        return self._size

    def __getitem__(self, index):
        self._check_bounds(index)
        return self._data[index]

    def __setitem__(self, index, value):
        self._check_bounds(index)
        self._data[index] = value

    def __repr__(self):
        return f"ArrayList({self.to_array()}, capacity={self._capacity})"
