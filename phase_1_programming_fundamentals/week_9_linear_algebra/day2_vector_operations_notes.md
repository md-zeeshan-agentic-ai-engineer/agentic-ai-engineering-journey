# Day 2 - Vector Operations

## Overview
In this lesson, we learned basic operations on vectors which are essential for Machine Learning and AI.

---

## Vector Addition

### Definition
Vector addition means adding corresponding elements of two vectors.

### Formula
[x1, y1] + [x2, y2] = [x1 + x2, y1 + y2]

### Example
v1 = [1, 2]  
v2 = [3, 4]  

Result → [4, 6]

---

## Scalar Multiplication

### Definition
Scalar multiplication means multiplying a vector by a number (scalar).

### Formula
k × [x, y] = [kx, ky]

### Example
2 × [1, 2] = [2, 4]

---

## Key Concepts

- Vector addition combines direction and magnitude  
- Scalar multiplication changes magnitude only  
- Direction remains same in scalar multiplication  

---

## AI / ML Connection

- Data is represented as vectors  
- Features are combined using vector addition  
- Weights scale inputs using scalar multiplication  

### Example (Linear Model)
prediction = w1*x1 + w2*x2  

This is vector operation in action

---

## Python Implementation

```python
import numpy as np

v1 = np.array([1, 2])
v2 = np.array([3, 4])

print("Addition:", v1 + v2)
print("Scalar:", 2 * v1)