# Polynomial Regression Notes

## Phase 2 - Week 15 - Day 1

---

# What is Linear Regression?

Linear Regression is a supervised machine learning algorithm used to predict a continuous numerical value by finding the best-fit straight line through the data.

It assumes that there is a **linear relationship** between the input feature (X) and the target variable (Y).

The equation of Linear Regression is:

\[
y = mx + b
\]

Where:
- y = Predicted output
- x = Input feature
- m = Slope of the line
- b = Intercept

Linear Regression works well only when the relationship between the variables is approximately a straight line.

---

# Why Does Linear Regression Fail?

Linear Regression fails when the relationship between the input and output is not linear.

Many real-world datasets have curved or complex patterns that cannot be represented by a straight line.

When a straight line is used to fit curved data:
- Prediction error increases.
- The model underfits the data.
- Important patterns are ignored.
- Accuracy decreases.

Therefore, Linear Regression is not suitable for every regression problem.

---

# Linear vs Non-linear Relationship

## Linear Relationship

A linear relationship means that the output changes at a constant rate as the input changes.

Characteristics:
- Straight-line pattern
- Constant rate of change
- Simple to model
- Best suited for Linear Regression

Examples:
- Hours studied vs marks (approximately)
- Distance traveled at constant speed
- Fixed salary increase

---

## Non-linear Relationship

A non-linear relationship means that the output does not change at a constant rate.

Characteristics:
- Curved pattern
- Variable rate of change
- More complex
- Better suited for Polynomial Regression

Examples:
- Salary growth with experience
- Population growth
- Car depreciation
- Business sales growth

---

# What is Polynomial Regression?

Polynomial Regression is an extension of Linear Regression that models non-linear relationships by creating polynomial features.

Instead of using only x, it also uses higher powers such as:

- x²
- x³
- x⁴

General equation:

\[
y = b + m_1x + m_2x^2 + m_3x^3 + ...
\]

Although the relationship between X and Y becomes curved, the model is still considered a linear model because it remains linear in its coefficients.

Polynomial Regression can fit curved datasets much better than Linear Regression.

---

# Real-Life Use Cases

## 1. Salary Prediction

Employee salary often increases faster as experience grows.

---

## 2. House Price Prediction

House prices may increase non-linearly depending on location and demand.

---

## 3. Population Growth

Population usually grows exponentially rather than linearly.

---

## 4. Sales Forecasting

Business sales often increase rapidly during promotions and festivals.

---

## 5. Student Performance

Learning improvement is usually fast at first and slows over time.

---

# Advantages of Polynomial Regression

- Models curved relationships effectively.
- More flexible than Linear Regression.
- Higher prediction accuracy on non-linear datasets.
- Can capture complex patterns.
- Easy to implement using Scikit-learn.

---

# Limitations of Polynomial Regression

- Can overfit when the polynomial degree is too high.
- More computationally expensive than Linear Regression.
- Sensitive to outliers.
- Choosing the correct polynomial degree can be difficult.
- Less interpretable than simple Linear Regression.

---

# When to Use Polynomial Regression

Use Polynomial Regression when:

- Data has a curved trend.
- Linear Regression produces poor results.
- Scatter plots show a non-linear relationship.
- Higher prediction accuracy is required.

---

# When Not to Use Polynomial Regression

Avoid Polynomial Regression when:

- The relationship is already linear.
- The dataset is very small.
- A high polynomial degree causes overfitting.
- Simplicity and interpretability are more important.

---

# Key Differences

| Linear Regression | Polynomial Regression |
|-------------------|----------------------|
| Fits a straight line | Fits a curve |
| Uses only x | Uses x, x², x³, ... |
| Simple model | More flexible model |
| Lower complexity | Higher complexity |
| May underfit curved data | Better for curved data |

---

# Summary

- Linear Regression assumes a straight-line relationship.
- Many real-world datasets are non-linear.
- Polynomial Regression introduces polynomial features to model curves.
- It improves prediction accuracy on non-linear datasets.
- Selecting an appropriate polynomial degree is important to avoid overfitting.

---

# Interview Questions

1. What is Linear Regression?
2. Why does Linear Regression fail on curved datasets?
3. What is a non-linear relationship?
4. What is Polynomial Regression?
5. How is Polynomial Regression different from Linear Regression?
6. Give three real-life applications of Polynomial Regression.
7. What are the advantages of Polynomial Regression?
8. What are the limitations of Polynomial Regression?
9. When should Polynomial Regression be used?
10. What is underfitting?

---

# End of Notes