"""
Activity Selection Problem Algorithm Explained Step-by-Step
-----------------------------------------------------------
The Activity Selection Problem is a classic greedy algorithm that finds the maximum number of 
non-overlapping activities that can be performed. Given a set of activities with start and end times,
the goal is to select the maximum number of activities that don't conflict with each other. This problem
demonstrates the greedy approach where making locally optimal choices leads to a globally optimal solution,
and is fundamental for scheduling, resource allocation, and interval optimization problems.

Here is how the process works:

1. **Sort by End Time**: Sort all activities by their ending times in ascending order.
   - activities.sort(key=lambda x: x[1])
   - This ensures we always consider activities that finish earliest first
   - Early finishing activities leave more room for subsequent activities

2. **Initialize Selection**: Start with an empty selection list and track the last selected end time.
   - selected = [] (stores chosen activities)
   - last_end = 0 (tracks when the last selected activity ended)
   - Begin with the assumption that no activity has been selected yet

3. **Greedy Choice**: Always select the activity with the earliest end time that doesn't conflict.
   - For each activity in sorted order, check if it can start after the last selected activity ends
   - If start_time >= last_end_time, the activity is compatible and can be selected
   - This greedy choice is proven to be optimal for this problem

4. **Compatibility Check**: Ensure no overlap between selected activities.
   - Check if current activity's start time >= previous activity's end time
   - If compatible: add to selection and update last_end time
   - If not compatible: skip this activity and continue to next one

5. **Update State**: After selecting an activity, update the last end time.
   - last_end = current_activity.end_time
   - This becomes the new constraint for future activity selections
   - Maintains the non-overlapping invariant throughout the process

6. **Optimal Solution**: The greedy approach guarantees the maximum number of activities.
   - Always choosing the earliest-ending compatible activity leaves maximum room for future selections
   - This local optimization leads to global optimality
   - Returns the maximum possible number of non-overlapping activities

Example: activities = [(1,4), (3,5), (0,6), (5,7), (8,9), (5,9)]
- Sorted by end time: [(1,4), (3,5), (0,6), (5,7), (8,9), (5,9)]
- Selection process: Choose (1,4), skip (3,5) and (0,6), choose (5,7), choose (8,9)
- Result: [(1,4), (5,7), (8,9)] - 3 activities selected

Time Complexity: O(n log n) due to sorting, where n is the number of activities
Space Complexity: O(1) excluding the output list, O(n) including the result
Greedy Property: Selecting earliest-ending activity is always safe and optimal

This algorithm demonstrates how greedy strategies can solve optimization problems efficiently
when the greedy choice property and optimal substructure are satisfied, making it essential
for understanding scheduling algorithms and interval-based optimization problems.
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
