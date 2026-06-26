import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Dataset
X = np.array([1, 2, 3, 4, 5, 6, 7, 8]).reshape(-1, 1)
y = np.array([45, 50, 55, 60, 68, 72, 78, 85])

# Model
model = LinearRegression()

model.fit(X, y)

# Prediction
y_pred = model.predict(X)

# Visualization
plt.figure(figsize=(8,5))

## Original points
plt.scatter(X, y, label="Actual Data")

## Regression Line
plt.plot(X, y_pred, label="Best Fit Line")

plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Linear Regression Visualization")

plt.legend()
plt.grid()

plt.savefig("regression_plot.png")
print("Plot saved successfully!")