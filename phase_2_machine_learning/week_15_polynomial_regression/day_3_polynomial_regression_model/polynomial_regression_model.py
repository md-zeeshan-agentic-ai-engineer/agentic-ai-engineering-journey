# 1. Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# 2. Load dataset
df = pd.read_csv("student_scores.csv")

# 3. Features and target
X = df[["Hours"]]
y = df[["Scores"]]

# 4. Train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size = 0.2,
    random_state = 42
)

# 5. Polynomial features
poly = PolynomialFeatures(degree=2)
X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)

# 6. Train model
model = LinearRegression()
model.fit(X_train_poly, y_train)

# 7. Predictions
y_pred = model.predict(X_test_poly)

# 8. Evaluation
print("MAE:", mean_absolute_error(y_test, y_pred))
print("MSE:", mean_squared_error(y_test, y_pred))
print("r2_Score:", r2_score(y_test, y_pred))

# 9. Visualization
plt.scatter(X, y, color="blue")

X_plot = X.sort_values(by="Hours")
X_plot_poly = poly.transform(X_plot)

plt.plot(X_plot, model.predict(X_plot_poly), color="red")

plt.xlabel("Hours")
plt.ylabel("Scores")
plt.title("Polynomial Regression")
plt.show()