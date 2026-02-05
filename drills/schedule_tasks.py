"""
## Problem Statement

Implement a factory task scheduler that manages a list of tasks with varying urgency levels 
and efficiently retrieves the highest-priority task for execution. The system must support 
adding tasks, extracting the next task to execute, and peeking at the highest-priority task 
without removing it. This tests understanding of priority queues, data structure design, and 
efficient scheduling algorithms.

## Whiteboard Coding Challenge Notes

* For this problem, I'm using a **Max-Heap Priority Queue with Registry Tracking**:

This approach combines a priority queue for efficient extraction with a hash map for O(1) 
duplicate detection. The max-heap ensures the highest-urgency task is always at the root, 
enabling O(log n) extraction and insertion.

* Key Concepts:

  - Why use a max-heap instead of a simple list?
A max-heap provides O(log n) insertion and extraction compared to O(n) linear search. For 
systems with thousands of tasks, this logarithmic performance is critical. The heap property 
(parent > children) ensures the highest-urgency task is always accessible in constant time.

  - Why maintain a separate task_registry (hash map)?
The registry enables O(1) duplicate detection when adding new tasks. Without it, checking 
if a task exists would require O(n) search through the queue. This trade-off (extra O(n) 
space) prevents duplicate entries and maintains data integrity in the scheduling system.

  - Why clamp urgency to a 1-10 range in __post_init__?
Normalizing urgency values prevents invalid states (e.g., urgency = 15 or 0) from reaching 
the comparison logic. This is a defensive programming practice that ensures the urgency 
scale is always meaningful and prevents unexpected comparison behavior.

  - Why implement __lt__ with inverted comparison (> instead of <)?
The custom comparison method reverses the natural ordering: urgency 10 < urgency 1. This 
converts the standard heap (min-heap) into a max-heap behavior where higher urgency tasks 
have priority. This is more intuitive than storing negative values.

* Logic:

1. Initialize FactoryTask with task_id and urgency, clamping urgency to valid range
2. Implement comparison logic (__lt__) that inverts ordering for max-heap behavior
3. Create ScheduledTasks with both queue (for priority retrieval) and registry (for deduplication)
4. add_task: Validate no duplicate exists, insert into heap, register in hash map
5. get_next_task: Extract max from heap, remove from registry, return task
6. peek_next_task: View next task without modifying queue state

* **30-Second Pitch**:

We're building a factory task scheduler using a max-heap priority queue paired with a hash 
map registry. When a new task arrives, we check the registry for duplicates in constant time, 
then insert it into the heap. When the factory needs the next task, we extract the highest-urgency 
item from the heap root—that's logarithmic. The combination of O(log n) queue operations and O(1) 
deduplication gives us an efficient, scalable scheduling system.

* **Rapid-Fire Version**:

- Max-heap priority queue for O(log n) insertion/extraction
- Hash map registry for O(1) duplicate detection
- Custom __lt__ comparison inverts natural order (urgency 10 is "less than" urgency 1)
- Urgency clamping in __post_init__ ensures valid 1-10 scale
- Separate peek/extract operations for flexible task inspection

* **Ultra-Minimal One-Liner**:

- Max-heap with registry deduplication: O(log n) scheduling with O(1) duplicate detection.

* **Complexity Analysis**:

- **Time Complexity:** 
  - add_task: O(log n) heap insertion + O(1) registry insert = O(log n)
  - get_next_task: O(log n) heap extraction + O(1) registry delete = O(log n)
  - peek_next_task: O(1) to access heap root
  
- **Space Complexity:** O(n) for heap + O(n) for registry = O(n) total

* **Use Cases**:

Manufacturing job scheduling, cloud task scheduling, operating system process scheduling, 
customer service ticketing systems—any domain where tasks have priority and must be processed 
in urgency order while preventing duplicate work.

"""

from dataclasses import dataclass
from typing import List, Optional

from .priority_queue import MaxHeapPriorityQueue


@dataclass
class FactoryTask:
    """Simplified factory task with minimal metadata."""
    task_id: str
    urgency: int  # 1-10 scale (10 = highest)

    def __post_init__(self) -> None:
        # Clamp urgency to 1-10 range
        self.urgency = max(1, min(10, self.urgency))

    def __lt__(self, other: 'FactoryTask') -> bool:
        """Compare by urgency (descending)."""
        return self.urgency > other.urgency

    def __repr__(self) -> str:
        return f"FactoryTask(id={self.task_id}, urgency={self.urgency})"

@dataclass
class ScheduledTasks:
    """Represents the current state of scheduled factory tasks."""
    queue: MaxHeapPriorityQueue
    task_registry: dict[str, FactoryTask]

    def add_task(self, task: FactoryTask) -> 'ScheduledTasks':
        """Add a new task and return updated scheduled tasks."""
        if task.task_id in self.task_registry:
            raise ValueError(f"Task {task.task_id} already exists")
        self.queue.insert(task, task.urgency)
        self.task_registry[task.task_id] = task
        return self

    def get_next_task(self) -> Optional[FactoryTask]:
        """Extract and return the highest-priority task."""
        result = self.queue.extract_max()
        if result:
            _, task = result
            if task.task_id in self.task_registry:
                del self.task_registry[task.task_id]
            return task
        return None

    def peek_next_task(self) -> Optional[FactoryTask]:
        """Peek at the next task without removing it."""
        result = self.queue.peek()
        return result[1] if result else None

def create_scheduled_tasks() -> ScheduledTasks:
    """Initialize an empty scheduled tasks object."""
    return ScheduledTasks(
        queue=MaxHeapPriorityQueue(),
        task_registry={}
    )

def schedule_tasks(tasks: List[FactoryTask]) -> ScheduledTasks:
    """Create a scheduled tasks object from a list of factory tasks."""
    scheduled = create_scheduled_tasks()
    for task in tasks:
        scheduled.add_task(task)
    return scheduled

def add_task_to_schedule(scheduled: ScheduledTasks, task: FactoryTask) -> ScheduledTasks:
    """Add a task to the schedule and return the updated scheduled tasks object."""
    return scheduled.add_task(task)
