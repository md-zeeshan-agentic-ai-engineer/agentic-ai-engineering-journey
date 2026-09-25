# Complete Code written by Md Zeeshan Quadri

## 1. Imports
## 2. Load the Dataset
## 3. Select Features and Target
## 4. Split the Data
## 5. Handle Missing Values
## 6. One-Hot Encode Categorical Features
## 7. Check the Final Data

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv("dataset/titanic/train.csv")

df.head()


X = df[
    [
        "Pclass",
        "Sex",
        "Age",
        "SibSp",
        "Parch",
        "Fare",
        "Embarked"
    ]
].copy()

y = df["Survived"]


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size = 0.2,
    random_state = 42,
    stratify = y
)


age_median = X_train["Age"].median()

X_train["Age"] = X_train["Age"].fillna(age_median)
X_test["Age"] = X_test["Age"].fillna(age_median)


embarked_mode = X_train["Embarked"].mode()[0]

X_train["Embarked"] = X_train["Embarked"].fillna(embarked_mode)
X_test["Embarked"] = X_train["Embarked"].fillna(embarked_mode)



X_train = pd.get_dummies(
    X_train,
    columns=["Sex", "Embarked"],
    drop_first = True
)

X_test = pd.get_dummies(
    X_test,
    columns=["Sex", "Embarked"],
    drop_first = True
)


print("Training Shape:", X_train.shape)
print("Test Shape:", X_test.shape)

print("\nMissing values in training:")
print(X_train.isnull().sum())

print("\nMissing values in test:")
print(X_test.isnull().sum())


import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv("dataset/titanic/train.csv")

df.head()


X = df[
    [
        "Pclass",
        "Sex",
        "Age",
        "SibSp",
        "Parch",
        "Fare",
        "Embarked"
    ]
].copy()

y = df["Survived"]


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size = 0.2,
    random_state = 42,
    stratify = y
)


age_median = X_train["Age"].median()

X_train["Age"] = X_train["Age"].fillna(age_median)
X_test["Age"] = X_test["Age"].fillna(age_median)


embarked_mode = X_train["Embarked"].mode()[0]

X_train["Embarked"] = X_train["Embarked"].fillna(embarked_mode)
X_test["Embarked"] = X_test["Embarked"].fillna(embarked_mode)


X_train = pd.get_dummies(
    X_train,
    columns = ["Sex", "Embarked"],
    drop_first = True
)

X_test = pd.get_dummies(
    X_test,
    columns = ["Sex", "Embarked"],
    drop_first = True
)


print("Training Shape:", X_train.shape)
print("Test Shape:", X_test.shape)

print("\nMissing Values in training:")
print(X_train.isnull().sum())

print("\nMissing Values in Test:")
print(X_test.isnull().sum())

