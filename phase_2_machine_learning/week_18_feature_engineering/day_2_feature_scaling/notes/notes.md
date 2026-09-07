# Day 2 — Feature Scaling

## Today's Goal

By the end of today, I will be able to:

- Explain why feature scaling is important.
- Understand the difference between StandardScaler, MinMaxScaler, and RobustScaler.
- Scale numerical features using Scikit-learn.
- Compare original and scaled data.
- Know when to use each scaling method.

---

# Part 1 — What is Feature Scaling?

## Definition

Feature Scaling is the process of bringing numerical features to a similar range.

It helps Machine Learning algorithms treat all numerical features fairly instead of giving more importance to features with larger values.

---

## Example

Imagine a dataset:

| Feature | Value |
|---------|------:|
| Age | 25 |
| Salary | 700000 |

Here:

- Age ranges from **18–60**
- Salary ranges from **20,000–2,000,000**

The salary values are much larger than the age values.

Many Machine Learning algorithms pay more attention to **Salary** than **Age** simply because Salary has much larger numerical values.

Feature Scaling solves this problem by converting numerical features to a similar scale.

---

# Why is Feature Scaling Important?

## Without Scaling

- Large-value features dominate the model.
- Distance calculations become inaccurate.
- Gradient Descent becomes slower.
- Some Machine Learning models perform poorly.

## With Scaling

- Faster model training.
- Better convergence.
- Improved model accuracy.
- Fair contribution from all numerical features.

---

# Algorithms That Need Feature Scaling

These algorithms depend on distance calculations or gradient optimization, so feature scaling is important.

- K-Nearest Neighbors (KNN)
- K-Means Clustering
- Logistic Regression
- Neural Networks
- Support Vector Machine (SVM)
- Principal Component Analysis (PCA)

---

# Algorithms That Usually Don't Need Feature Scaling

These algorithms split data using thresholds instead of distances.

- Decision Tree
- Random Forest
- XGBoost
- LightGBM

---

# Key Points

- Feature Scaling brings numerical features into a similar range.
- It prevents large-value features from dominating smaller-value features.
- Scaling improves the performance of distance-based algorithms.
- Tree-based algorithms generally do not require feature scaling.

# Part 2 — StandardScaler

## Formula

z = x - μ / σ

Where:

- x = Original value
- μ = Mean
- σ = Standard Deviation

## What does StandardScaler do?

StandardScaler transforms numerical data so that:

- Mean = 0
- Standard Deviation = 1

This makes all numerical features have a common scale while preserving the original data distribution.

---

## Example

### Original Values

```
Age
20
25
30
35
40
```

Mean = 30

Standard Deviation ≈ 7.07

### After StandardScaler

```
-1.41
-0.71
 0.00
 0.71
 1.41
```

---

## Advantages

- Makes features comparable.
- Speeds up gradient descent.
- Improves convergence of machine learning algorithms.
- Works well when data is approximately normally distributed.

---

## Best Used With

- Logistic Regression
- Linear Regression
- Support Vector Machine (SVM)
- K-Nearest Neighbors (KNN)
- Neural Networks
- PCA

---

# Part 3 — MinMaxScaler

## Formula

x - min / max - min

## What does MinMaxScaler do?

MinMaxScaler rescales all values to a fixed range.

Default range:

```
0 to 1
```

- Minimum value becomes 0.
- Maximum value becomes 1.
- All other values lie between 0 and 1.

---

## Example

### Original Values

```
10
20
30
40
50
```

### After MinMaxScaler

```
0.00
0.25
0.50
0.75
1.00
```

---

## Advantages

- Keeps the relationship between values.
- Easy to interpret.
- Useful when algorithms expect values in a fixed range.

---

## Limitation

MinMaxScaler is sensitive to outliers.

If one value is extremely large, the remaining values get compressed.

---

## Best Used With

- Neural Networks
- Deep Learning
- Image Data
- Distance-based algorithms

---

# Part 4 — RobustScaler

## What does RobustScaler use?

Instead of Mean and Standard Deviation, RobustScaler uses:

- Median
- Interquartile Range (IQR)

Because of this, it is much less affected by outliers.

---

## When should we use RobustScaler?

Use RobustScaler when the dataset contains outliers.

---

## Example

Original Values

```
20
25
30
35
1000
```

Here,

```
1000
```

is an outlier.

StandardScaler is heavily affected by this value.

RobustScaler scales the data using Median and IQR, so the outlier has much less influence.

---

## Advantages

- Resistant to outliers.
- Produces better scaling when extreme values exist.
- Preserves useful information from the majority of data.

---

## Best Used With

- Financial data
- Salary data
- Real estate prices
- Sensor data
- Any dataset containing outliers

---

# Comparison

| Scaler | Output Range | Uses | Best For |
|---------|--------------|------|----------|
| StandardScaler | Mean = 0, Std = 1 | Mean & Standard Deviation | Normally distributed data |
| MinMaxScaler | 0 to 1 | Minimum & Maximum | Neural Networks, Image Data |
| RobustScaler | Median & IQR | Median & Interquartile Range | Data with Outliers |

---

# Quick Revision

### StandardScaler

- Mean becomes 0.
- Standard deviation becomes 1.
- Best for normally distributed data.

### MinMaxScaler

- Converts values between 0 and 1.
- Sensitive to outliers.
- Best for neural networks and image data.

### RobustScaler

- Uses Median and IQR.
- Handles outliers effectively.
- Best for datasets containing extreme values.