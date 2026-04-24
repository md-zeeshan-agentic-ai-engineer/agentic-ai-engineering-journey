# Week 11 - Day 5: Distributions (Normal Distribution)

## What is a Distribution?

A distribution shows how data values are spread or arranged.

In Machine Learning, understanding data distribution is very important because models learn patterns based on it.

---

##  Normal Distribution (Gaussian Distribution)

The normal distribution is a bell-shaped curve where:

* Most values are near the mean (center)
* Fewer values are far from the mean
* The distribution is symmetric

### Real-world Examples:

* Student marks
* Human height
* Salaries

---

## Key Concepts

### 1. Mean (μ)

* The center of the data

### 2. Standard Deviation (σ)

* Measures how spread out the data is

* Low σ → data is tightly packed

* High σ → data is widely spread

---

## Normal Distribution Formula

f(x) = (1 / (σ√2π)) * e^(-(x - μ)² / (2σ²))

---

## 68-95-99.7 Rule

* 68% of data lies within 1σ
* 95% of data lies within 2σ
* 99.7% of data lies within 3σ

Helps in detecting outliers

---

## Outliers

* Values far from the mean
* Usually rare events

Example:

* Fraud transactions
* Abnormal sensor readings

---

## Python Implementation

```python
import numpy as np
import matplotlib.pyplot as plt

# Generate normal distribution data
data = np.random.normal(loc=0, scale=1, size=1000)

# Plot histogram
plt.hist(data, bins=30)
plt.savefig("graph.png")
```

---

## Key Learning

* Most real-world data follows normal distribution
* ML models assume normal distribution in many cases
* Understanding distribution = better model performance

---

## Real AI/ML Use Cases

* Noise modeling
* Error analysis
* Weight initialization
* Data preprocessing

---

## Conclusion

Normal distribution is one of the most important concepts in statistics and machine learning.
It helps us understand how data behaves and how to detect unusual patterns.

---

## Output

* Generated file: `graph.png`
* Shows a bell-shaped histogram

---

## Status

Day 5 Completed
