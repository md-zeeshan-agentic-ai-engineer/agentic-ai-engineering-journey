# 1. Print matrices and its shape
import numpy as np

A = np.array([[1, 2, 5, 8],
              [3, 4, 4, 5],
              [5, 7, 9, 9],
              [4, 8, 9, 3]])

B = np.array([[5, 5, 6, 7, 8, 7, 6],
              [7, 5, 6, 7, 4, 3, 8]])

print(A)
print(B)

print("Shape:", A.shape)
print("Shape:", B.shape)
print("First row:", A[0])
print("Element (1,1):", A[1][1])



# 2. Element access
import numpy as np
 
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

print(A[2][1])  # 8
print(A[2][0])  # 7
print(A[1][2])  # 6
print(A[0][2])  # 3
print(A[1][0])  # 4


# 3. Some examples
import numpy as np

# 2x2 Matrix
A = np.array([[1, 2],
              [3, 4]])

# 2x3 Matrix
B = np.array([[1, 2, 3],
              [4, 5, 6]])

# 3x1 Matrix
C = np.array([[1],
              [2],
              [3]])

# Print all matrices
print("Matrix A:\n", A)
print("Shape:", A.shape)

print("\nMatrix B:\n", B)
print("Shape:", B.shape)

print("\nMatrix C:\n", C)
print("Shape:", C.shape)