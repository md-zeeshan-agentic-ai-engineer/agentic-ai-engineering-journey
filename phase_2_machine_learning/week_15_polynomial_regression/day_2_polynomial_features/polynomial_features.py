# Polynomial Features


import numpy as np
from sklearn.preprocessing import PolynomialFeatures

X = np.array([[1],
              [2],
              [3],
              [4]])

poly = PolynomialFeatures(degree=3)

X_poly = poly.fit_transform(X)

print(X_poly)

## Degree = 2
X = np.array([[5]])

poly = PolynomialFeatures(degree=2)

X_poly = poly.fit_transform(X)

print(X_poly)

## Degree 3
X = np.array([[5]])

poly = PolynomialFeatures(degree=3)

X_poly = poly.fit_transform(X)

print(X_poly)