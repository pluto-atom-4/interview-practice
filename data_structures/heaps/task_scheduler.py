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


def measure_heap_performance(heap_class, tasks, extract_method):
    heap = heap_class()
    start_insert = time.time()
    for task in tasks:
        heap.insert(task)
    end_insert = time.time()

    extracted = []
    start_extract = time.time()
    while True:
        try:
            extracted.append(getattr(heap, extract_method)().priority)
        except IndexError:
            break
    end_extract = time.time()

    return {
        "insert_time": end_insert - start_insert,
        "extract_time": end_extract - start_extract,
        "order": extracted,
    }


def run_trials(num_trials=5, num_tasks=1000):
    min_insert_times = []
    min_extract_times = []
    max_insert_times = []
    max_extract_times = []

    for _ in range(num_trials):
        tasks = [
            Task(
                name=f"Task-{i}", priority=random.randint(1, 100), timestamp=time.time()
            )
            for i in range(num_tasks)
        ]
        min_result = measure_heap_performance(MinHeap, tasks, "extract_min")
        max_result = measure_heap_performance(MaxHeap, tasks, "extract_max")

        min_insert_times.append(min_result["insert_time"])
        min_extract_times.append(min_result["extract_time"])
        max_insert_times.append(max_result["insert_time"])
        max_extract_times.append(max_result["extract_time"])

    return {
        "min_insert_avg": sum(min_insert_times) / num_trials,
        "min_extract_avg": sum(min_extract_times) / num_trials,
        "max_insert_avg": sum(max_insert_times) / num_trials,
        "max_extract_avg": sum(max_extract_times) / num_trials,
    }


def plot_performance_comparison(results):
    labels = ["Insert", "Extract"]
    min_times = [results["min_insert_avg"], results["min_extract_avg"]]
    max_times = [results["max_insert_avg"], results["max_extract_avg"]]

    x = range(len(labels))
    plt.figure(figsize=(8, 5))
    plt.bar(x, min_times, width=0.4, label="MinHeap", align="center", color="skyblue")
    plt.bar(
        [i + 0.4 for i in x],
        max_times,
        width=0.4,
        label="MaxHeap",
        align="center",
        color="salmon",
    )
    plt.xticks([i + 0.2 for i in x], labels)
    plt.ylabel("Time (seconds)")
    plt.title("Heap Performance Comparison (Average over Trials)")
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    simulate_task_scheduling()
    results = run_trials(num_trials=5, num_tasks=1000)
    plot_performance_comparison(results)
