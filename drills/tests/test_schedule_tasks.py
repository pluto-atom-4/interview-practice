import pytest

from drills.schedule_tasks import (
    FactoryTask,
    ScheduledTasks,
    add_task_to_schedule,
    create_scheduled_tasks,
    schedule_tasks,
)


def test_factory_task_urgency_clamping():
    t1 = FactoryTask("A", 15)
    t2 = FactoryTask("B", -5)
    assert t1.urgency == 10
    assert t2.urgency == 1

def test_add_and_peek_task():
    scheduled = create_scheduled_tasks()
    t1 = FactoryTask("A", 5)
    scheduled.add_task(t1)
    assert scheduled.peek_next_task() == t1

def test_add_duplicate_task_raises():
    scheduled = create_scheduled_tasks()
    t1 = FactoryTask("A", 5)
    scheduled.add_task(t1)
    with pytest.raises(ValueError):
        scheduled.add_task(FactoryTask("A", 7))

def test_get_next_task_priority_order():
    t1 = FactoryTask("A", 5)
    t2 = FactoryTask("B", 8)
    t3 = FactoryTask("C", 3)
    scheduled = schedule_tasks([t1, t2, t3])
    assert scheduled.get_next_task() == t2
    assert scheduled.get_next_task() == t1
    assert scheduled.get_next_task() == t3
    assert scheduled.get_next_task() is None

def test_add_task_to_schedule():
    scheduled = create_scheduled_tasks()
    t1 = FactoryTask("A", 4)
    t2 = FactoryTask("B", 9)
    scheduled = add_task_to_schedule(scheduled, t1)
    scheduled = add_task_to_schedule(scheduled, t2)
    assert scheduled.peek_next_task() == t2

def test_peek_next_task_empty():
    scheduled = create_scheduled_tasks()
    assert scheduled.peek_next_task() is None

def test_get_next_task_empty():
    scheduled = create_scheduled_tasks()
    assert scheduled.get_next_task() is None
