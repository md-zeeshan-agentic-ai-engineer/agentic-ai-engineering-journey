# Day 4 - Compare Models

## Objective

### Compare Linear Regression and Polynomial Regression.
### Dataset: Synthetic Curved Dataset
### Models: Linear Regression, Polynomial Regression
### Evaluation: MAE, MSE, R2 Score


import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

np.random.seed(42)

X = np.linspace(0, 10, 100).reshape(-1, 1)

y = X**2 + np.random.randn(100,1)*5


linear_model = LinearRegression()

linear_model.fit(X, y)

linear_pred = linear_model.predict(X)


poly_model = make_pipeline(
    PolynomialFeatures(degree=2),
    LinearRegression()
)

poly_model.fit(X, y)

poly_pred = poly_model.predict(X)



plt.figure(figsize=(10,6))

plt.scatter(X, y, color="blue", label="Original Data")

plt.plot(X, y, color="red", label="Linear Regression")
plt.plot(X, y, color="green", label="Polynomial Regression")

plt.legend()
plt.title("Linear vs Polynomial Regression")

plt.xlabel("X")
plt.ylabel("y")
plt.show()


print("Linear Regression")

print("MAE :",mean_absolute_error(y,linear_pred))
print("MSE :",mean_squared_error(y,linear_pred))
print("R2 :",r2_score(y,linear_pred))

print()

print("Polynomial Regression")

print("MAE :",mean_absolute_error(y,poly_pred))
print("MSE :",mean_squared_error(y,poly_pred))
print("R2 :",r2_score(y,poly_pred))


# Comparison

## Linear Regression

### Fits a straight line.
### Best for linear data.
### Simple and fast.
### Cannot fit curved data well.

## Polynomial Regression

### Fits curved relationships.
### Uses polynomial features.
### Better for non-linear data.
### High polynomial degree may overfit.

## Conclusion

### Polynomial Regression performs better on curved datasets because it can learn non-linear patterns.