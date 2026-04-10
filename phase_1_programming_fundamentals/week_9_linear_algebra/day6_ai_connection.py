# AI Connection

import numpy as np

# Input (vector)
x = np.array([1, 2])

# Weights (matrix)
W = np.array([[1, 2],
              [3, 4]])

# Bias
b = np.array([1, 1])

# Output
y = np.dot(W, x) + b

print(y)

# Output = AI ka decision