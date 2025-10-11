# Big-O Notation Explained

Big-O notation describes the efficiency of algorithms, especially how their running time or space requirements grow as input size increases. It is a key concept in coding interviews and software engineering.

## Why is Big-O Important?
- Helps compare algorithms
- Predicts performance for large inputs
- Shows scalability and bottlenecks

## Common Big-O Complexities
| Complexity   | Example Algorithm         | Description                       |
|-------------|--------------------------|-----------------------------------|
| O(1)        | Hash table lookup        | Constant time                     |
| O(log n)    | Binary search            | Logarithmic time                  |
| O(n)        | Linear search            | Time grows with input size        |
| O(n log n)  | Merge sort               | Efficient sorting                 |
| O(n^2)      | Bubble sort, nested loops| Slower for large inputs           |

## Example from This Project
- **Merge Sort** (`algorithms/sorting/merge_sort.py`):
  - Time Complexity: **O(n log n)**
  - Space Complexity: **O(n)**
- Other scripts also include searching and data structure operations, each with their own Big-O characteristics.

## How to Use This Knowledge in Interviews
- Mention the Big-O of your solution
- Justify your choice of algorithm
- Discuss trade-offs (speed vs. memory)

---
For more details, see comments in each script explaining their algorithm and complexity.
