# Day 2 - Polynomial Features

## Objective

Learn how Polynomial Features transform a linear model into a model capable of learning non-linear (curved) relationships.

---

# Why Polynomial Features?

Linear Regression can only fit a straight line.

Many real-world datasets have curved relationships.

Polynomial Features create new features such as x², x³, etc., allowing Linear Regression to fit curves while still using a linear model internally.

---

# Degree 2

Original feature:

x

Transformed features:

1, x, x²

Equation:

y = b + m₁x + m₂x²

Example:

x = 5

Output:

[1, 5, 25]

---

# Degree 3

Transformed features:

1, x, x², x³

Equation:

y = b + m₁x + m₂x² + m₃x³

Example:

x = 5

Output:

[1, 5, 25, 125]

---

# Higher-Degree Polynomial Features

Degree 4:

1, x, x², x³, x⁴

Degree 5:

1, x, x², x³, x⁴, x⁵

Higher degrees allow more complex curves but can also lead to overfitting.

---

# PolynomialFeatures in Scikit-learn

Import:

```python
from sklearn.preprocessing import PolynomialFeatures
```

Example:

```python
import numpy as np
from sklearn.preprocessing import PolynomialFeatures

X = np.array([[1],
              [2],
              [3],
              [4]])

poly = PolynomialFeatures(degree=3)

X_poly = poly.fit_transform(X)

print(X_poly)
```

Output:

```
[[ 1.  1.  1.  1.]
 [ 1.  2.  4.  8.]
 [ 1.  3.  9. 27.]
 [ 1.  4. 16. 64.]]
```

Columns:

- First column → Bias (1)
- Second column → x
- Third column → x²
- Fourth column → x³

---

# Advantages

- Learns curved relationships
- Improves prediction on non-linear data
- Easy to use with Linear Regression
- Simple preprocessing technique

---

# Limitations

- High-degree polynomials may overfit
- More features increase model complexity
- Sensitive to noisy data

---

# Real-World Applications

- House Price Prediction
- Population Growth
- Sales Forecasting
- Temperature Prediction
- Medical Data Analysis
- Engineering Curves

---

# Key Takeaways

- Polynomial Features create new features like x² and x³.
- Linear Regression becomes capable of fitting curves.
- Degree 2 creates [1, x, x²].
- Degree 3 creates [1, x, x², x³].
- Higher degrees provide more flexibility but may cause overfitting.

---

# Mini Exercise

For x = 5

Degree 2:

```
[1, 5, 25]
```

Degree 3:

```
[1, 5, 25, 125]
```

---

# Summary

Polynomial Features transform input data into higher-degree features, allowing Linear Regression to model non-linear relationships without changing the learning algorithm.