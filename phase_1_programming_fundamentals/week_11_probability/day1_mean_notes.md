# Day 1 — Mean (Average)

## Definition

The mean (average) is the sum of all values divided by the total number of values.

## Formula

Mean = (x1 + x2 + x3 + ... + xn) / n

---

## Examples

### Example 1

Data: [1, 2, 3, 4, 5]
Mean = 3

### Example 2

Data: [10, 20, 30]
Mean = 20

### Example 3

Data: [5, 5, 5, 5]
Mean = 5

### Example 4 (Outlier Case)

Data: [1, 100, 1000]
Mean = 367
 Outlier affects the mean heavily

### Example 5

Data: [100, 200, 300, 400, 500]
Mean = 300

---

## Python Code

```python
import numpy as np

data = [1, 2, 3, 4, 5]
print(np.mean(data))
```

---

## Important Insight

* Mean is sensitive to outliers
* Large extreme values can distort the result

---

## AI/ML Connection

* Mean represents the center of data
* Used in data normalization
* Helps models understand data distribution
* Important for machine learning preprocessing

---

## Summary

* Mean = average value of data
* Easy to compute
* Useful but affected by outliers
* Core concept in AI and data science

-----