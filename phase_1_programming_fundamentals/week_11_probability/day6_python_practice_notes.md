# Day 6 – Python Practice (Statistics + ML Basics)

## Objective
Learn and implement Mean, Variance, and Standard Deviation using Python (NumPy) and understand their role in Machine Learning.

---

## Core Concepts

### 1. Mean (Average)
- Center of data
- Formula:
  Mean = (sum of values) / n

Example:
[2, 4, 6] → Mean = 4

---

### 2. Variance
- Measures spread of data
- High variance → data is scattered
- Low variance → data is stable

---

### 3. Standard Deviation
- Square root of variance
- Shows how much data deviates from mean

---

## Complete Python Code

```python
import numpy as np

# STEP 1: Basic Data
data = [1, 2, 3, 4, 5]
print("Basic Data")
print("Mean:", np.mean(data))
print("Variance:", np.var(data))
print("Std Dev:", np.std(data))

# STEP 2: Custom Data
data = [10, 20, 30, 40, 50]
print("\nCustom Data")
print("Mean:", np.mean(data))
print("Variance:", np.var(data))

# STEP 3: Random Data (Real ML Scenario)
random_data = np.random.randint(1, 100, size=10)
print("\nRandom Data:", random_data)
print("Mean:", np.mean(random_data))
print("Variance:", np.var(random_data))
print("Std Dev:", np.std(random_data))

# STEP 4: Mini Project (Student Marks Analyzer)
marks = [45, 67, 89, 56, 72, 90]
print("\nMarks Analysis")
print("Mean:", np.mean(marks))
print("Variance:", np.var(marks))
print("Std Dev:", np.std(marks))

# STEP 5: Experiment (Important Insight)
data1 = [10, 10, 10, 10]
data2 = [1, 50, 100, 200]

print("\nExperiment")
print("Variance (data1):", np.var(data1))
print("Variance (data2):", np.var(data2))