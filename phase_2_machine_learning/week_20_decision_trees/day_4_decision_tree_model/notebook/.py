import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv("../dataset/titanic/train.csv")

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

X = pd.get_dummies(
    X,
    columns = ["Sex", "Embarked"],
    drop_first = True
)


X["Age"] = X["Age"].fillna(X["Age"].median())

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size = 0.2,
    random_state = 42
)


model = DecisionTreeClassifier(
    random_state = 42
)


model.fit(X_train, y_train)


predictions = model.predict(X_test)


accuracy = accuracy_score(y_test, predictions)

print("Test Accuracy:", accuracy)