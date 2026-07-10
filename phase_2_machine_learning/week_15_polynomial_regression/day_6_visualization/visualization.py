import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

# Sample Data
X = np.array([1, 2, 3, 4, 5, 6, 7, 8]).reshape(-1, 1)
y = np.array([3, 5, 8, 15, 24, 35, 48, 63])

# Linear Regression
linear = LinearRegression()
linear.fit(X, y)

# Polynomial Regression
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)
poly_model = LinearRegression()
poly_model.fit(X_poly, y)

# Smooth curve
X_test = np.linspace(1,8,100).reshape(-1,1)

plt.scatter(X, y, label="Original Data")
plt.plot(X_test,
         linear.predict(X_test),
         label="Linear Regression")

plt.plot(X_test,
         poly_model.predict(poly.transform(X_test)),
         label="Polynomial Regression")

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Linear vs Polynomial Regression")
plt.legend()
plt.show()