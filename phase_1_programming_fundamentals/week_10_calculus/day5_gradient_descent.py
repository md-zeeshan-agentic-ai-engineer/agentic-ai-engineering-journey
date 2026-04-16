# x^2
x = 5
lr = 0.1

for i in range(10):
    grad = 2*x  # derivative of x^2
    x = x - lr*grad
    print(x)



#  x^2 + 4x + 4
x = 5
lr = 0.1

for i in range(10):
    grad = 2*x + 4
    x = x - lr*grad
    print(x)