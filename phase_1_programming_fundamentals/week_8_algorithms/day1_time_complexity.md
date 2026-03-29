# Day 1: Time Complexity

## What is Time Complexity?

Time Complexity is a way to measure how the running time of an algorithm increases as the input size (n) increases.

It does not measure actual time (seconds), but how the number of operations grows.

---

## Why Time Complexity is Important?

* Helps in writing efficient code
* Important for handling large data
* Crucial for coding interviews
* Used in system design and real-world applications

---

## Common Time Complexities

| Complexity | Name         | Example                 |
| ---------- | ------------ | ----------------------- |
| O(1)       | Constant     | Accessing array element |
| O(log n)   | Logarithmic  | Binary Search           |
| O(n)       | Linear       | Loop through array      |
| O(n log n) | Linearithmic | Merge Sort              |
| O(n²)      | Quadratic    | Nested loops            |

---

## Important Rules

1. **Ignore constants**

   * O(2n) → O(n)
   * O(n + 100) → O(n)

2. **Sequential loops → Add**

   * O(n) + O(n) = O(n)

3. **Nested loops → Multiply**

   * O(n) × O(n) = O(n²)

4. **Drop lower order terms**

   * O(n² + n) → O(n²)

---

## Examples

### Example 1: O(n)

```python
for i in range(n):
    print(i)
# Time Complexity: O(n)
```

---

### Example 2: O(n²)

```python
for i in range(n):
    for j in range(n):
        print(i, j)
# Time Complexity: O(n²)
```

---

### Example 3: O(log n)

```python
i = 1
while i < n:
    print(i)
    i *= 2
# Time Complexity: O(log n)
```

---

### Example 4: O(n log n)

```python
for i in range(n):
    j = 1
    while j < n:
        print(i, j)
        j *= 2
# Time Complexity: O(n log n)
```

---

## Key Insight

Time Complexity = Total number of operations performed by the code.

Always ask:
"How many times is this loop running?"

---

## Conclusion

Understanding time complexity helps in:

* Writing optimized code
* Solving problems efficiently
* Becoming a better software engineer

This is one of the most important concepts in programming and algorithms.