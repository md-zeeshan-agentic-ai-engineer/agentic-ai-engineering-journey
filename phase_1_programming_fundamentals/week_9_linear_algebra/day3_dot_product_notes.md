# Day 3 – Dot Product (Linear Algebra)

## What is Dot Product?

The dot product is a mathematical operation between two vectors that results in a single number (scalar).

### Formula:
a · b = a₁b₁ + a₂b₂

### Example:
[1, 2] · [3, 4] = (1×3) + (2×4) = 3 + 8 = 11

---

## Geometric Meaning

Dot product also represents the relationship between two vectors using angle:

a · b = |a||b|cosθ

- If θ = 0° → vectors are in same direction → maximum value  
- If θ = 90° → vectors are perpendicular → dot product = 0  
- If θ = 180° → vectors are opposite → negative value  

---

## Key Insights

- Dot product measures **similarity between vectors**
- Larger value → more similar direction  
- Zero → no relation (orthogonal vectors)  
- Negative → opposite direction  

---

## Connection with AI / ML

Dot product is widely used in Machine Learning:

- Similarity between embeddings  
- Recommendation systems  
- Search ranking  
- Neural networks calculations  

Example:
User vector · Item vector → similarity score

---

## Python Implementation

```python
import numpy as np

v1 = np.array([1, 2])
v2 = np.array([3, 4])

dot = np.dot(v1, v2)
print(dot)