# Logistic Regression Theory

## 1. Why Linear Regression Fails for Classification

Linear Regression is used to predict continuous numerical values. It is not suitable for classification because:

- It predicts values from negative infinity to positive infinity.
- Classification requires discrete class labels such as 0 and 1.
- Predicted values can be less than 0 or greater than 1, which cannot represent probabilities.
- It is sensitive to outliers.
- It does not provide a proper decision boundary for classification.

Example:
A Linear Regression model may predict:
- -0.5
- 0.8
- 1.4

These outputs are not valid probabilities.

---

# 2. What is Logistic Regression?

Logistic Regression is a supervised machine learning algorithm used for classification problems.

It predicts the probability that a data point belongs to a particular class. The output is always between 0 and 1.

It first calculates a linear equation:

z = w₁x₁ + w₂x₂ + ... + b

Then it passes this value through the Sigmoid Function to convert it into a probability.

Example:
- Spam Detection
- Disease Prediction
- Fraud Detection
- Customer Churn Prediction

---

# 3. Sigmoid Function

The Sigmoid Function converts any real number into a value between 0 and 1.

Formula:

σ(z) = 1 / (1 + e^(-z))

Where:
- σ(z) = Sigmoid Function
- z = Linear equation output
- e = Euler's number (≈ 2.71828)

Properties:
- Output is always between 0 and 1.
- Produces probability values.
- Smooth S-shaped curve.
- Used in binary classification.

Example values:

| z | Sigmoid(z) |
|---|------------|
| -5 | 0.007 |
| -2 | 0.119 |
| 0 | 0.500 |
| 2 | 0.881 |
| 5 | 0.993 |

---

# 4. Probability Interpretation

The output of Logistic Regression represents probability.

Examples:

- 0.95 → Very likely Spam
- 0.80 → Spam
- 0.60 → Spam
- 0.49 → Not Spam
- 0.20 → Not Spam
- 0.05 → Definitely Not Spam

Higher probability means a higher chance that the sample belongs to Class 1.

---

# 5. Decision Threshold (0.5)

A threshold is used to convert probability into a class label.

Rule:

- If Probability ≥ 0.5 → Class 1
- If Probability < 0.5 → Class 0

Example:

| Probability | Prediction |
|-------------|------------|
| 0.90 | Class 1 |
| 0.75 | Class 1 |
| 0.51 | Class 1 |
| 0.49 | Class 0 |
| 0.20 | Class 0 |

The threshold can be changed depending on the application, but 0.5 is the most common.

---

# Summary

- Linear Regression is not suitable for classification.
- Logistic Regression predicts probabilities.
- The Sigmoid Function converts linear outputs into probabilities.
- The output always lies between 0 and 1.
- A threshold (usually 0.5) is used to predict the final class.