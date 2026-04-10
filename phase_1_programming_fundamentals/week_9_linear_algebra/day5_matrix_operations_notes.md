# Day 5 - Matrix Operations

## 1. Matrix Addition

### Rule:
Matrix addition is done element-wise.

Two matrices can only be added if they have the same size.

### Example:
A = [[1, 2],
     [3, 4]]

B = [[5, 6],
     [7, 8]]

A + B = [[6, 8],
         [10, 12]]

---

## 2. Matrix Multiplication (Core Concept)

### Rule:
- Rows of A × Columns of B
- Inner dimensions must match

### Formula:
C = A × B

### Example:
A = [1, 2]  
B = [[3],
     [4]]

A · B = (1×3 + 2×4) = 11

---

## 3. Python Implementation

```python
import numpy as np

A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])

# Addition
print("Addition:\n", A + B)

# Multiplication
print("Multiplication:\n", np.dot(A, B))

# Matmul
print("Matmul:\n", np.matmul(A, B))