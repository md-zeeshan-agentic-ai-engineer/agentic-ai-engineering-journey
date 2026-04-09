# Day 4: Matrices Basics

## What is a Matrix?

A matrix is a collection of numbers arranged in rows and columns.

Example:
[[1, 2],
[3, 4]]

Rows = horizontal
Columns = vertical

---

## Shape of a Matrix

Shape tells the size of a matrix.

Format:
(rows, columns)

Example:
[[1, 2],
[3, 4]]

Shape = (2, 2)

---

## Creating Matrix in Python

import numpy as np

A = np.array([[1, 2],
[3, 4]])

print(A)

---

## Different Matrix Shapes

2x2 Matrix:
A = np.array([[1, 2],
[3, 4]])

2x3 Matrix:
B = np.array([[1, 2, 3],
[4, 5, 6]])

3x1 Matrix:
C = np.array([[1],
[2],
[3]])

---

## Checking Shape

print(A.shape)
print(B.shape)
print(C.shape)

---

## Accessing Elements

Format:
A[row][column]

Example:
A = np.array([[1, 2, 3],
[4, 5, 6],
[7, 8, 9]])

print(A[2][1])  # Output: 8

Explanation:
Row 2 → [7, 8, 9]
Column 1 → 8

---

## Accessing Rows

print(A[0])  # First row

---

## Key Concepts

* Matrix = data structure
* Shape = size of matrix
* Row = data point
* Column = feature

---

## AI Connection

* Data = vectors
* Weights = matrices
* Neural networks = matrix multiplication

---

## Summary

* Learned matrix basics
* Understood shape and indexing
* Practiced different matrix types
* Connected matrices to AI

---

## Status

Day 4 Completed ✅