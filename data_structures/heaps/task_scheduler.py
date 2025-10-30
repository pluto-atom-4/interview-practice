"""
Min Heap vs Max Heap performance using task scheduling
---
- MinHeap schedules low-priority tasks first (e.g. background jobs), while MaxHeap prioritizes urgent tasks.
- Inserting and extracting 1000 tasks showed similar performance, with MaxHeap slightly faster on extraction.
- Visualizations show how each heap orders tasks differently — MinHeap starts with the smallest priorities, MaxHeap with the largest.
"""

import random
import time

import matplotlib.pyplot as plt


class Task:
    def __init__(self, name, priority, timestamp):
        self.name = name
        self.priority = priority
        self.timestamp = timestamp

    def __lt__(self, other):
        return self.priority < other.priority

    def __gt__(self, other):
        return self.priority > other.priority

    def __repr__(self):
        return f"{self.name} (P:{self.priority}, T:{self.timestamp})"


class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, task):
        self.heap.append(task)
        self._bubble_up(len(self.heap) - 1)

    def extract_min(self):
        if not self.heap:
            raise IndexError("Heap is empty")
        if len(self.heap) == 1:
            return self.heap.pop()
        min_task = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._bubble_down(0)
        return min_task

    def _bubble_up(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if self.heap[index] < self.heap[parent]:
                self.heap[index], self.heap[parent] = (
                    self.heap[parent],
                    self.heap[index],
                )
                index = parent
            else:
                break

    def _bubble_down(self, index):
        length = len(self.heap)
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            smallest = index

            if left < length and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < length and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest == index:
                break

            self.heap[index], self.heap[smallest] = (
                self.heap[smallest],
                self.heap[index],
            )
            index = smallest


class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, task):
        self.heap.append(task)
        self._bubble_up(len(self.heap) - 1)

    def extract_max(self):
        if not self.heap:
            raise IndexError("Heap is empty")
        if len(self.heap) == 1:
            return self.heap.pop()
        max_task = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._bubble_down(0)
        return max_task

    def _bubble_up(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if self.heap[index] > self.heap[parent]:
                self.heap[index], self.heap[parent] = (
                    self.heap[parent],
                    self.heap[index],
                )
                index = parent
            else:
                break

    def _bubble_down(self, index):
        length = len(self.heap)
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            largest = index

            if left < length and self.heap[left] > self.heap[largest]:
                largest = left
            if right < length and self.heap[right] > self.heap[largest]:
                largest = right

            if largest == index:
                break

            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            index = largest


def simulate_task_scheduling(num_tasks=1000):
    tasks = [
        Task(name=f"Task-{i}", priority=random.randint(1, 100), timestamp=time.time())
        for i in range(num_tasks)
    ]

    min_heap = MinHeap()
    max_heap = MaxHeap()

    # Measure insertion time
    start_min = time.time()
    for task in tasks:
        min_heap.insert(task)
    end_min = time.time()

    start_max = time.time()
    for task in tasks:
        max_heap.insert(task)
    end_max = time.time()

    # Measure extraction time
    min_order = []
    start_min_ext = time.time()
    while True:
        try:
            min_order.append(min_heap.extract_min().priority)
        except IndexError:
            break
    end_min_ext = time.time()

    max_order = []
    start_max_ext = time.time()
    while True:
        try:
            max_order.append(max_heap.extract_max().priority)
        except IndexError:
            break
    end_max_ext = time.time()

    # Plot performance
    plt.figure(figsize=(10, 4))
    plt.bar(
        ["MinHeap Insert", "MaxHeap Insert"],
        [end_min - start_min, end_max - start_max],
        color="skyblue",
    )
    plt.bar(
        ["MinHeap Extract", "MaxHeap Extract"],
        [end_min_ext - start_min_ext, end_max_ext - start_max_ext],
        color="orange",
    )
    plt.title("Heap Performance Comparison")
    plt.ylabel("Time (seconds)")
    plt.show()

    # Plot scheduling order
    plt.figure(figsize=(10, 4))
    plt.plot(min_order, label="MinHeap Order", color="green")
    plt.plot(max_order, label="MaxHeap Order", color="red")
    plt.title("Task Execution Order")
    plt.xlabel("Execution Step")
    plt.ylabel("Priority")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    simulate_task_scheduling()
