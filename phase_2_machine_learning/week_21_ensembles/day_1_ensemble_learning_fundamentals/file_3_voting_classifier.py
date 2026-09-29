from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

from sklearn.ensemble import VotingClassifier
from sklearn.metrics import accuracy_score


# Load dataset
X, y = load_iris(return_X_y=True)

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# Define models
logistic_model = make_pipeline(
    StandardScaler(),
    LogisticRegression(max_iter=1000)
)

knn_model = make_pipeline(
    StandardScaler(),
    KNeighborsClassifier(n_neighbors=5)
)

tree_model = DecisionTreeClassifier(
    random_state=42,
    max_depth=4
)


# Create voting ensemble
voting_model = VotingClassifier(
    estimators=[
        ("logistic", logistic_model),
        ("knn", knn_model),
        ("tree", tree_model)
    ],
    voting="hard"
)


# Train
voting_model.fit(X_train, y_train)


# Predict
y_pred = voting_model.predict(X_test)


# Evaluate
accuracy = accuracy_score(y_test, y_pred)

print("Voting Ensemble Accuracy:", accuracy)