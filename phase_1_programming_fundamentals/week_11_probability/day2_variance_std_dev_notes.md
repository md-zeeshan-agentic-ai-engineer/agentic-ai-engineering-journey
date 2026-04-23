# Day 2 — Variance and Standard Deviation

## 🔹 What is Variance?

Variance measures how much the data is spread out from the mean.

* High variance → data is widely spread
* Low variance → data is close to the mean

---

## Formula

Variance:
Var(X) = (1/n) * Σ (xi - μ)²

Where:

* xi = each data point
* μ = mean
* n = number of values

---

## Standard Deviation

Standard deviation is the square root of variance.

Std Dev (σ) = √Var(X)

* It represents the average distance from the mean
* Easier to interpret because it is in the same unit as data

---

## Example 1

Data: [2, 4, 6]

* Mean = 4
* Differences = (-2, 0, 2)
* Squares = (4, 0, 4)
* Variance = (4 + 0 + 4) / 3 = 2.67
* Std Dev ≈ 1.63

---

## Example 2

Data: [1, 1, 1, 1, 1]

* Mean = 1
* Variance = 0
* Std Dev = 0

👉 All values are the same → no spread

---

## Example 3

Data: [1, 5, 10, 20, 50]

* Mean = 17.2
* Variance ≈ 309.36
* Std Dev ≈ 17.59

👉 Data is highly spread

---

## Intuition (Important for ML)

* High variance → unstable model (risk of overfitting)
* Low variance → stable model (may underfit)

In Machine Learning:

* Large fluctuations in loss → high variance
* Smooth learning → low variance

---

## Python Example

```python
import numpy as np

data = [2, 4, 6]

print("Mean:", np.mean(data))
print("Variance:", np.var(data))
print("Std Dev:", np.std(data))
```

---

## Key Takeaways

* Mean = center of data
* Variance = spread of data
* Standard deviation = average distance from mean

---

## Why This Matters

* Core concept in Machine Learning
* Used in model evaluation and training stability
* Helps understand data distribution and behavior

---

Status:
Day 2 Completed
