"""
Activity Selection Problem
---
- Goal: Select the maximum number of non-overlapping activities from a list of start and end times.
- Greedy Strategy: Always pick the activity that ends earliest and doesn’t overlap with previously selected ones.
"""


def select_activities(activities):
    # activities: list of tuples (start, end)
    sorted_acts = sorted(activities, key=lambda x: x[1])
    selected = []
    last_end = 0

    for start, end in sorted_acts:
        if start >= last_end:
            selected.append((start, end))
            last_end = end

    return selected
