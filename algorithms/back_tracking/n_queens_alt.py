"""
### 🔍 Key Differences

| Feature               | Your Version                                                                 | Earlier Version                                                  |
|-----------------------|------------------------------------------------------------------------------|------------------------------------------------------------------|
| **Board Representation** | 2D list of strings (`"#"` and `"Q"`)                                         | 1D list of integers (column index per row)                       |
| **Conflict Tracking**    | Uses `cols`, `diags1`, `diags2` boolean arrays                              | Checks conflicts by scanning previous rows                       |
| **Diagonal Indexing**    | `diag1 = row - col + n - 1`, `diag2 = row + col`                            | Uses `abs(r - row) == abs(c - col)`                              |
| **Result Format**        | Returns full 2D board (`list[list[list[str]]]`)                             | Returns list of column positions (`list[list[int]]`)             |
| **Performance**          | Faster due to constant-time conflict checks                                 | Slightly slower due to repeated scanning                         |
| **Readability**          | More visual and intuitive for board layout                                  | More compact and memory-efficient                                |



### 🧪 Which One Should You Use?
✅ 2D list version is better for:
- Visualizing the board
- Teaching or explaining the algorithm
- Fast performance with large n

### ✅ 1D list version is better for:
- Compact memory usage
- Simpler logic for small n
- Formatting solutions later with a helper
"""


def backtrack(
    row: int,
    n: int,
    state: list[list[str]],
    res: list[list[list[str]]],
    cols: list[bool],
    diags1: list[bool],
    diags2: list[bool],
):
    if row == n:
        res.append([list(row) for row in state])
        return

    for col in range(n):
        diag1 = row - col + n - 1
        diag2 = row + col
        if not cols[col] and not diags1[diag1] and not diags2[diag2]:
            state[row][col] = "Q"
            cols[col] = diags1[diag1] = diags2[diag2] = True
            backtrack(row + 1, n, state, res, cols, diags1, diags2)
            state[row][col] = "#"
            cols[col] = diags1[diag1] = diags2[diag2] = False


def n_queens(n: int) -> list[list[list[str]]]:
    state = [["#" for _ in range(n)] for _ in range(n)]
    cols = [False] * n
    diags1 = [False] * (2 * n - 1)
    diags2 = [False] * (2 * n - 1)
    res = []
    backtrack(0, n, state, res, cols, diags1, diags2)

    return res
