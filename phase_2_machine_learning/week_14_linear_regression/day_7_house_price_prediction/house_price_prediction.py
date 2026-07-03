# 1. Dataset
## Use the California Housing Dataset from Scikit-Learn.

from sklearn.datasets import fetch_california_housing

housing = fetch_california_housing()


## Convert into DataFrame.

import pandas as pd

df = pd.DataFrame(housing.data,columns=housing.feature_names)
df["Price"] = housing.target

df.to_csv("california_housing.csv", index=False)
print("CSV saved successfully!")

df.head()

# 2. Explore Dataset
df.shape
df.info()
df.describe()
df.isnull().sum()

# 3. Train/Test Split
from sklearn.model_selection import train_test_split

X = df.drop("Price", axis = 1)
y = df["Price"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size = 0.2,
    random_state = 42
)

print("Training Features:", X_train.shape)
print("Testing Features:", X_test.shape)
print("Training Labels:", y_train.shape)
print("Testing Labels:", y_test.shape)


# 4. Model
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)

# 5. Predictions
predictions = model.predict(X_test)
print(predictions[:10])

# 6.Evaluate Model
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score

print(mean_absolute_error(y_test, predictions))
print(mean_squared_error(y_test, predictions))
print(r2_score(y_test, predictions))

# 7. Interpret Coefficients
coef = pd.DataFrame({
    "Feature": X.columns,
    "Coefficient": model.coef_
})

print(coef.sort_values(by="Coefficient"))