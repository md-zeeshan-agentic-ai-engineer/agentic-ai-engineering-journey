# Matrix Operations (Addition, Multiplication)

import numpy as np

A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

# Addition
print("Addition:\n", A + B)

# Multiplication
print("Multiplication:\n", np.dot(A, B))
print("matmul:\n", np.matmul(A, B))