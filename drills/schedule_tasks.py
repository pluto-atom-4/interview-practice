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
