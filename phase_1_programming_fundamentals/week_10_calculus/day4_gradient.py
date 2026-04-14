def grad(x, y):
    return 2*x, 2*y

x, y = 3, 4
gx, gy = grad(x, y)

print("Gradient:", gx, gy)