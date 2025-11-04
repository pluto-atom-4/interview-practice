"""
Strassen's Matrix Multiplication Algorithm Explained Step-by-Step
----------------------------------------------------------------
Strassen's algorithm is a divide-and-conquer matrix multiplication method that achieves better asymptotic
time complexity than the standard O(n³) algorithm. It recursively divides matrices into quadrants and
uses 7 multiplications instead of 8 by cleverly combining addition and subtraction operations. This
algorithm is fundamental for understanding advanced matrix computations and divide-and-conquer optimization.

Here is how the process works:

1. **Base Case**: Handle 1x1 matrices directly.
   - When n = 1, return [[A[0][0] * B[0][0]]]
   - This stops the recursion and performs simple scalar multiplication
   - Essential for preventing infinite recursion in the divide-and-conquer approach

2. **Matrix Division**: Split each nxn matrix into four (n/2)x(n/2) submatrices.
   - A = [[A11, A12], [A21, A22]], B = [[B11, B12], [B21, B22]]
   - Each quadrant represents a quarter of the original matrix
   - This enables parallel processing of smaller matrix operations

3. **Seven Products Calculation**: Compute M1 through M7 using specific combinations.
   - M1 = (A11 + A22) * (B11 + B22)  # Main diagonal contribution
   - M2 = (A21 + A22) * B11          # Lower-left influence
   - M3 = A11 * (B12 - B22)          # Upper-right influence
   - M4 = A22 * (B21 - B11)          # Lower-right influence
   - M5 = (A11 + A12) * B22          # Upper row influence
   - M6 = (A21 - A11) * (B11 + B12)  # Cross-diagonal effect
   - M7 = (A12 - A22) * (B21 + B22)  # Cross-diagonal effect

4. **Result Quadrants Construction**: Combine the seven products to form result quadrants.
   - C11 = M1 + M4 - M5 + M7  # Upper-left result quadrant
   - C12 = M3 + M5            # Upper-right result quadrant
   - C21 = M2 + M4            # Lower-left result quadrant
   - C22 = M1 - M2 + M3 + M6  # Lower-right result quadrant

5. **Matrix Assembly**: Merge the four result quadrants into the final matrix.
   - Concatenate C11 and C12 horizontally for upper half
   - Concatenate C21 and C22 horizontally for lower half
   - Stack upper and lower halves vertically to form complete result

6. **Recursive Application**: Apply the same process to each submatrix multiplication.
   - Each of the 7 products (M1-M7) recursively calls strassen() on smaller matrices
   - Recursion continues until base case (1x1 matrices) is reached
   - Results bubble up through recursive calls to build final solution

Example: Multiply two 4x4 matrices
- Division: Split into four 2x2 submatrices each
- Products: Calculate 7 specific combinations of submatrix products
- Assembly: Combine results to form final 4x4 matrix
- Result: Matrix multiplication with reduced computational complexity

Time Complexity: O(n^log₂(7)) ≈ O(n^2.807) vs O(n³) for standard multiplication
Space Complexity: O(n²) for storing submatrices and intermediate results
Practical Note: Overhead makes it beneficial only for large matrices (typically n > 64-128)

This algorithm demonstrates how mathematical insight can reduce computational complexity through
clever reorganization of operations, making it essential for high-performance matrix computations.
"""

def add_matrix(A, B):
    n = len(A)
    return [[A[i][j] + B[i][j] for j in range(n)] for i in range(n)]

def sub_matrix(A, B):
    n = len(A)
    return [[A[i][j] - B[i][j] for j in range(n)] for i in range(n)]

def strassen(A, B):
    n = len(A)
    if n == 1:
        return [[A[0][0] * B[0][0]]]

    mid = n // 2
    A11 = [row[:mid] for row in A[:mid]]
    A12 = [row[mid:] for row in A[:mid]]
    A21 = [row[:mid] for row in A[mid:]]
    A22 = [row[mid:] for row in A[mid:]]

    B11 = [row[:mid] for row in B[:mid]]
    B12 = [row[mid:] for row in B[:mid]]
    B21 = [row[:mid] for row in B[mid:]]
    B22 = [row[mid:] for row in B[mid:]]

    M1 = strassen(add_matrix(A11, A22), add_matrix(B11, B22))
    M2 = strassen(add_matrix(A21, A22), B11)
    M3 = strassen(A11, sub_matrix(B12, B22))
    M4 = strassen(A22, sub_matrix(B21, B11))
    M5 = strassen(add_matrix(A11, A12), B22)
    M6 = strassen(sub_matrix(A21, A11), add_matrix(B11, B12))
    M7 = strassen(sub_matrix(A12, A22), add_matrix(B21, B22))

    C11 = add_matrix(sub_matrix(add_matrix(M1, M4), M5), M7)
    C12 = add_matrix(M3, M5)
    C21 = add_matrix(M2, M4)
    C22 = add_matrix(sub_matrix(add_matrix(M1, M3), M2), M6)

    new_matrix = []
    for i in range(mid):
        new_matrix.append(C11[i] + C12[i])
    for i in range(mid):
        new_matrix.append(C21[i] + C22[i])

    return new_matrix
