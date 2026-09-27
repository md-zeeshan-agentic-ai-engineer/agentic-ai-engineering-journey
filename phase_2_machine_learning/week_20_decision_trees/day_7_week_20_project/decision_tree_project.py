import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import(
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report
)

df = pd.read_csv("../dataset/titanic/train.csv")

df.columns
df.shape
df.dtypes
df.describe()
df.isnull().sum()
df.info()


df = df.drop(columns=["PassengerId", "Name", "Ticket", "Cabin"])

df.head()

df.isnull().sum()


X = df.drop(columns="Survived")
y = df["Survived"]

X.shape, y.shape

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size = 0.2,
    random_state = 42,
    stratify = y
)