from sklearn.model_selection import train_test_split

x = [[1], [2], [3], [4], [5], [6], [7], [8]]
y = [0, 0, 0, 1, 1, 1, 1, 1]

x_train, x_test, y_train, y_test = train_test_split(
    x,
    y,
    test_size = 0.2,
    random_state = 42
)

print("Training Data:", x_train)
print("Testing Data:", x_test)

print("Train size =", len(x_train))
print("Test size =", len(x_test))