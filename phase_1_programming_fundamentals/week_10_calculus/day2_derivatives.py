# Day 2 — Derivatives Basics

# Example functions and their derivatives

# f(x) = x^2 → derivative = 2x
def f1(x):
    return x**2

def df1(x):
    return 2*x


# f(x) = x^3 → derivative = 3x^2
def f2(x):
    return x**3

def df2(x):
    return 3*(x**2)


# f(x) = 3x^2 → derivative = 6x
def f3(x):
    return 3*(x**2)

def df3(x):
    return 6*x


# Test values
x = 5

print("f1(x):", f1(x), " df1(x):", df1(x))
print("f2(x):", f2(x), " df2(x):", df2(x))
print("f3(x):", f3(x), " df3(x):", df3(x))