from sklearn.model_selection import train_test_split

X = [[1], [2], [3], [4], [5], [6], [7], [8]]
y = [0, 0, 0, 1, 1, 1, 1, 1]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size = 0.2,
    random_state = 42
)

print("Training Data:", X_train)
print("Testing Data:", X_test)

print("Train size =", len(X_train))
print("Test size =", len(X_test))